import requests
import pandas as pd

def verify_email(email, api_key):
    if pd.isna(email) or email=="":
        return "Invalid"

    try:
        url=f"https://emailvalidation.abstractapi.com/v1/?api_key={api_key}&email={email}"
        res=requests.get(url)
        data=res.json
        return "valid" if data.get("deliverability")=="DELIVERABLE" else "Invalid"

    except:
        return "Unknown"

def verify_all_emails(df, api_key):
    df['Email Status']=df['Email'].apply(lambda x: verify_email(x, api_key))
    return df