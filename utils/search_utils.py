# utils/search_utils.py

import streamlit as st

def search_data(df):
    search_column = st.selectbox("Select column to search in:", df.columns.tolist())
    search_query = st.text_input("Enter search query:")

    if search_query:
        filtered_df = df[df[search_column].astype(str).str.contains(search_query, case=False, na=False)]
        return filtered_df
    return df

def advanced_search(df, search_fields, query):
    # Example function that uses pandas query method to allow complex queries.
    # Note: real implementation would need to handle errors and edge cases.
    query_string = ' & '.join(f"{field}.str.contains('{query}', case=False, na=False)" for field in search_fields)
    return df.query(query_string)

