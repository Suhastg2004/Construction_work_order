# Construction Work Order Generator

## Overview
The **Construction Work Order Generator** is a **Streamlit-based web application** that automates the creation of **detailed work orders** for construction projects. Using **Groq's DeepSeek R1 LLM**, the app takes **user inputs** (client details, labor, materials, and costs) and generates a **structured work order document** instantly.

## Features
- Interactive UI – Simple, user-friendly interface powered by **Streamlit**  
- AI-Powered Work Order Generation – Uses **Groq’s DeepSeek R1 model** for structured output  
- Auto-Calculation of Labor & Material Costs – Reduces manual effort  
- Dynamic Inputs – Supports multiple services, labor details, and material costs  
- Instant Output – Generates structured work orders with a click  

---

## Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Suhastg2004/Construction_work_order.git
cd Construction_work_order
```

### 2. Create a Virtual Environment
```bash
python3 -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r req.txt
```

---

## Dependencies (req.txt)
```text
langchain
langchain-groq
streamlit
```

---

## API Key Setup
1. Obtain a Groq API Key from [Groq Platform](https://groq.com).
2. Store it securely:
   - Option 1: Create a `.env` file and add:  
     ```
     GROQ_API_KEY=your_groq_api_key
     ```
   - Option 2: Set it as an environment variable:  
     ```bash
     export GROQ_API_KEY="your_groq_api_key"
     ```

---

## How to Run the Application
```bash
streamlit run app.py
```
- Open the **localhost URL** shown in the terminal.
- Fill in the work order details.
- Click **"Generate Work Order"** to see AI-generated results.

---

## Expected Output
Once the user fills in the details and clicks "Generate Work Order", the AI generates a **structured work order**, including:

- Client Information  
- Order Details  
- Work Description  
- Service & Labor Breakdown  
- Parts & Materials Used  
- Cost Summary (Tax, Other Costs, Total)  

---

## Future Improvements
- PDF Export for downloading work orders  
- Multi-user authentication for better access control  
- Database Integration to store and retrieve past work orders  

---


---

## Disclaimer
This project is for **educational purposes only** and does not replace professional contract management software.

---

## Contact
For any issues, reach out via [suhastg1282004@gmail.com](mailto:suhastg1282004@gmail.com).

