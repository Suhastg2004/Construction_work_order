import streamlit as st
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from langchain import PromptTemplate
from constants import GROQ_API_KEY

# Initialize Groq LLM
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="deepseek-r1-distill-llama-70b"
)

# Streamlit UI
st.title("🏗️ Construction Work Order Generator")

# Input Fields for Work Order Details
client_name = st.text_input("Client Name:")
order_number = st.text_input("Order Number:")
client_phone = st.text_input("Client Phone:")
customer_id = st.text_input("Customer ID:")
client_email = st.text_input("Client Email:")
order_received_by = st.text_input("Order Received By:")
order_date = st.date_input("Order Date:")
expected_start_date = st.date_input("Expected Start Date:")
expected_end_date = st.date_input("Expected End Date:")
work_authorized_by = st.text_input("Work Authorized By:")
work_description = st.text_area("Work Description:")
additional_comments = st.text_area("Additional Comments:")

# Input for Service and Labor
st.subheader("Service and Labor Details")
labor_rows = []
for i in range(3): 
    col1, col2, col3, col4 = st.columns(4)
    service_desc = col1.text_input(f"Service {i+1} Description")
    hours = col2.number_input(f"Hours {i+1}", min_value=0.0, format="%.2f")
    rate = col3.number_input(f"Rate {i+1}", min_value=0.0, format="%.2f")
    amount = hours * rate
    col4.write(f"Amount: ${amount:.2f}")
    labor_rows.append(f"{service_desc}, {hours} hours, ${rate}/hour, Total: ${amount:.2f}")

# Input for Materials
st.subheader("Parts and Materials Details")
material_rows = []
for i in range(3): 
    col1, col2, col3, col4 = st.columns(4)
    part_desc = col1.text_input(f"Material {i+1} Description")
    quantity = col2.number_input(f"Quantity {i+1}", min_value=0)
    price_per_unit = col3.number_input(f"Price per Unit {i+1}", min_value=0.0, format="%.2f")
    amount = quantity * price_per_unit
    col4.write(f"Amount: ${amount:.2f}")
    material_rows.append(f"{part_desc}, {quantity} units, ${price_per_unit}/unit, Total: ${amount:.2f}")

# Additional Cost Inputs
tax_rate = st.number_input("Tax Rate (%)", min_value=0.0, format="%.2f")
other_cost = st.number_input("Other Cost ($)", min_value=0.0, format="%.2f")


if st.button("Generate Work Order"):
    if client_name and order_number and work_description:
        formatted_prompt = f"""
        Generate a detailed construction work order with the following details:

        **Client Information**
        - Name: {client_name}
        - Phone: {client_phone}
        - Email: {client_email}
        - Customer ID: {customer_id}
        
        **Order Details**
        - Order Number: {order_number}
        - Order Received By: {order_received_by}
        - Order Date: {order_date}
        - Expected Start Date: {expected_start_date}
        - Expected End Date: {expected_end_date}
        - Work Authorized By: {work_authorized_by}

        **Work Description**
        {work_description}

        **Additional Comments**
        {additional_comments}

        **Service and Labor Details**
        {', '.join(labor_rows)}

        **Parts and Materials Details**
        {', '.join(material_rows)}

        **Cost Breakdown**
        - Tax Rate: {tax_rate}%
        - Other Cost: ${other_cost}
        """

        # Get LLM response
        response = llm.invoke([HumanMessage(content=formatted_prompt)])

        # Display the response
        st.subheader("Generated Work Order:")
        st.write(response.content)
    else:
        st.warning("Please fill in all required fields (Client Name, Order Number, Work Description).")
