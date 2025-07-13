import pandas as pd

def filter_leads(df, require_email=True, location=None, industry=None):
    if require_email:
        df=df[df['Email'].notna()]
    if location:
        df=df[df['Location'].str.contains(location, case=False, na=False)]
    if industry:
        df=df[df['Industry'].str.contains(industry, case=False, na=False)]

    return df