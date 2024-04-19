# utils/search_utils.py

import streamlit as st
import re
import pandas as pd

def simple_highlight(text, search_query):
    """Highlight the entire word containing the search query in DataFrame by adding double asterisks."""
    # Use regex to find whole words containing the search query and make them stand out with double asterisks
    regex = r'\b\w*{}[\w]*\b'.format(re.escape(search_query))
    highlight = lambda x: re.sub(regex, r'**\g<0>**', x, flags=re.IGNORECASE)
    return text.apply(lambda x: highlight(x) if isinstance(x, str) else x)


def search_data(df):
    search_column = st.selectbox("Select column to search in:", df.columns.tolist())
    search_query = st.text_input("Enter search query:")

    if search_query:
        # Perform the search and filter the dataframe
        filtered_df = df[df[search_column].astype(str).str.contains(search_query, case=False, na=False)]
        
        # Apply simple highlighting to the search column
        filtered_df[search_column] = simple_highlight(filtered_df[search_column], search_query)
        
        # Optionally, display the number of results here if you still want to show it within the function
        # st.write(f"Total results: {len(filtered_df)}")

        return filtered_df

    return df


# def search_data(df):
#     search_column = st.selectbox("Select column to search in:", df.columns.tolist())
#     search_query = st.text_input("Enter search query:")

#     if search_query:
#         filtered_df = df[df[search_column].astype(str).str.contains(search_query, case=False, na=False)]
#         return filtered_df
#     return df

def advanced_search(df, search_fields, query):
    # Example function that uses pandas query method to allow complex queries.
    # Note: real implementation would need to handle errors and edge cases.
    query_string = ' & '.join(f"{field}.str.contains('{query}', case=False, na=False)" for field in search_fields)
    return df.query(query_string)

