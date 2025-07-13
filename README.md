# SaaSquatch Leads Toolkit

A powerful, lightweight lead processing and CRM-preparation tool built using **Python** and **Streamlit**, developed for the **Caprae AI Readiness Challenge**.

This toolkit allows you to upload a CSV of company leads and quickly:
- Filter leads based on criteria
- Predict industry tags
- Format for CRM tools (like HubSpot)
- Verify email deliverability using Abstract API

  ---

## 💡 Features

✅ Upload CSV files with leads  
✅ Filter leads by:
- Email availability
- Location
- Industry

✅ Predict company industries (SaaS, Logistics, Retail, etc.)  
✅ Format output for HubSpot CRM  
✅ Verify email deliverability using [Abstract Email Verification API](https://www.abstractapi.com/email-verification-api)  
✅ Export cleaned + tagged CSV

---

## 🛠️ Tech Stack

- Python 3.x
- Streamlit
- Pandas
- Requests (for API calls)
- Abstract Email Verification API

---

## 📦 Folder Structure
📁 saasquatchleads-project/
├── app/
│ ├── lead_filter.py
│ ├── lead_tagger.py
│ ├── crm_exporter.py
│ └── email_verifier.py
├── sample_leads.csv
├── requirements.txt
├── streamlit_app.py
└── README.md

---

## 🚀 How to Run It

1. **Clone this repository**  
   
   git clone https://github.com/29SagunSingh/SaaSquatchleads.git
   cd SaaSquatchleads

2. **Install dependencies**
    pip install -r requirements.txt

3. **Launch the Streamlit App**
   streamlit run streamlit_app.py

4. **Use the web interface** to upload CSVs, filter leads, tag industries, verify emails, and export.

## 🔑 Get an Abstract API Key
Visit: https://www.abstractapi.com/email-verification-api
Sign up and copy your API key — paste it into the app when prompted to verify emails.

# 🏁 Submission for Caprae AI Readiness Challenge
This project demonstrates:
  1. Python + API integration
  2. Dashboard development using Streamlit
  3. Data cleaning, formatting, and enrichment
  4. Real-world CRM readiness workflow

