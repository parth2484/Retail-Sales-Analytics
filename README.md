# Retail Sales Data Engineering Pipeline

This project demonstrates an end-to-end Data Engineering workflow where sales data is cleaned, processed, stored, and visualized to generate business insights.

---

## ✅ What You Need Before Starting

### 1) Software Installations
| Tool | Purpose | Download Link |
|-----|---------|---------------|
| **Python** | Data cleaning & transformation | https://www.python.org/downloads/ |
| **MySQL Server + MySQL Workbench** | Database storage & SQL queries | https://dev.mysql.com/downloads/installer/ |
| **Power BI Desktop** | Dashboard & visualization | https://powerbi.microsoft.com/desktop/ |

### 2) Python Libraries to Install
Open Command Prompt and install:
  1.  pip install pandas
  2.  pip install mysql-connector-python


---

## 🧱 Project Steps (High-Level Workflow)

### **Step 1: Prepare Your Dataset**
Use any **retail or sales dataset** in CSV format (columns like date, product, quantity, and price).  
Save the file to your system for use in the pipeline.

---

### **Step 2: Create MySQL Database and Table**
Open **MySQL Workbench**:
1. Create a new database (e.g., `retail_sales`)
2. Create a table for storing sales data (columns matching your CSV)

---

### **Step 3: Load and Clean Data Using Python**
- Read the CSV file into Python
- Clean or adjust data (e.g., remove nulls, calculate totals)
- Connect to MySQL and insert the cleaned records

*(Code not included here — you will write based on your logic.)*

Sure ✅ Here is the **GitHub-ready section** you can paste directly into your README:

---

### **▶️ How to Run the ETL Script**

1. Open **Command Prompt / Terminal**
2. Navigate to the folder where `etl_pipeline.py` is located:

   ```
   cd scripts
   ```
3. Run the script:

   ```
   python etl_pipeline.py
   ```

#### **Expected Output**

If everything is set up correctly, you will see:

```
✅ Data loaded successfully into MySQL!
```



---

### **Step 4: Verify Data in MySQL**
Run SQL queries in Workbench to:
- Check total records
- Validate calculations
- Analyze product or date-wise metrics

---

### **Step 5: Create Dashboard in Power BI**

1. Open **Power BI Desktop**
2. Click **Get Data**
3. Choose:
   - **MySQL Database** (recommended), or
   - **Import CSV Directly** for quicker setup
4. Load your sales data

#### Create These Visuals:
| Visual | Purpose |
|-------|---------|
| **Card** | Display Total Revenue |
| **Bar Chart** | Show Top Selling Products |
| **Line Chart** | Display Daily/Monthly Sales Trend |

Arrange and format dashboard neatly.

---

## 🎯 Output / Final Result
You will have:
- A cleaned & structured sales dataset stored in MySQL
- A Power BI dashboard showing key business metrics:
  - Total revenue
  - Best-selling products
  - Sales trends over time

---

## 🧠 Skills Demonstrated
- Data Cleaning & Transformation
- SQL Database Design and Querying
- ETL Pipeline Understanding
- KPI Dashboard Creation in Power BI

---

## 🤝 Contributions
Contributions and suggestions are welcome.
