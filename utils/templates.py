# utils/templates.py

import streamlit as st

def common_header(title):
    st.title(title)
    st.markdown("### Analyze the data using the tools below")
    
def display_dataframe(df):
    # Set default arguments for displaying dataframes
    st.dataframe(df, width=None, height=450)  # Adjust height as needed