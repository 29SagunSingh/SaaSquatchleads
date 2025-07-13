import streamlit as st
import pandas as pd
from app.lead_filter import filter_leads
from app.lead_tagger import apply_tags
from app.crm_exporter import format_for_hubspot
from app.email_verifier import verify_all_emails

st.set_page_config(page_title="SaaSquatch Lead Toolkit", layout="wide")
st.title("SaaSquatch Lead Toolkit - Caprae AI Readiness Challenge")

uploaded_file=st.file_uploader("Upload your Leads CSV", type="csv")

if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.write("### Uploaded Data", df.head())

    with st.expander("Apply Filters"):
        require_email=st.checkbox("Require Email", value=True)
        location_filter=st.text_input("Filter by Location (optional)")
        industry_filter=st.text_input("Filter by Industry(optional")
        if st.button("Apply Filters"):
            df=filter_leads(df, require_email=require_email, location=location_filter, industry=industry_filter)
            st.success(f"Filtered down to {len(df)} rows")
            st.write(df.head())

    if st.button("Apply Industry Tagging"):
        df=apply_tags(df)
        st.success("Industry Tags Added")
        st.write(df.head())

    if st.button("Format for HubSpot"):
        df=format_for_hubspot(df)
        st.success("Formatted for CRM export")
        st.write(df.head())

    with st.expander("Verify Emails"):
        api_key=st.text_input("Enter your Abstract API Key", type="password")
        if st.button("Run Email Validation"):
            if api_key:
                df=verify_all_emails(df, api_key)
                st.success("Email status added")
                st.write(df.head())
            else:
                st.error("API Key required!")

    csv=df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Processed Leads", data=csv, file_name="processed_leads.csv", mime='text/csv')
