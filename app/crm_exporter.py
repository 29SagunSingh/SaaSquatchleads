def format_for_hubspot(df):
    df=df.rename(columns={
        'Company': 'Company Name',
        'Email': 'Email',
        'Phone': 'Phone Number'
    })
    cols=['Company Name', 'Email', 'Phone Number', 'Website', 'Location', 'Industry']
    for col in cols:
        if col not in df.columns:
            df[col]=''
    return df[cols]