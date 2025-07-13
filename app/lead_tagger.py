def tag_industry(company_name):
    if not isinstance(company_name, str):
        return "Unknown"
    name=company_name.lower()

    if "tech" in name or "cloud" in name:
        return "Saas"
    elif "mart" in name or "fresh" in name:
        return "Retail"
    elif "logi" in name or "ship" in name:
        return "Logistics"
    else:
        return "Other"

def apply_tags(df):
    df['Predicted Industry']=df['Company'].apply(tag_industry)
    return df