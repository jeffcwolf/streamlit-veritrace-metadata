import streamlit as st
from utils import data_processing, download_utils, filter_utils, search_utils, templates, visualisations, dataframe_tools, catalog_utils
import os
import pandas as pd

def app():
    st.title('EEBO Analysis Metadata (Beta)')
    st.write("Welcome to the EEBO analysis page. NOTE: All Metadata is raw and has not been cleaned or processed.")
    
    # Load and display the data
    df = data_processing.load_eebo_data()  # Ensure this function is imported correctly
    if df is not None and not df.empty:
        templates.display_dataframe(df)
    else:
        st.write("No data available.")