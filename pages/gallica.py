import streamlit as st
from utils import data_processing, download_utils, filter_utils, search_utils, templates, visualisations, dataframe_tools, catalog_utils
import os
import pandas as pd

def app():
    st.title('Gallica Analysis (BETA - Raw Metadata)')
    st.write("Welcome to the Gallica data source analysis page.")    
    
    # Load the data
    df = data_processing.load_gallica_data()  # Ensure this function is imported correctly
    

    if df is not None and not df.empty:
        templates.display_dataframe(df)
    else:
        st.write("No data available.")
    
    # Display the language distribution plot
    if st.button('Show Language Distribution'):
        catalog_utils.plot_language_distribution(df, 'language')
        
    # Add dataframe tools
    dataframe_tools.dataframe_toolbox(df)
    
    # Top hits
    catalog_utils.top_hits_by_author_and_title_gallica(df)
    
    # Display top n values for each column
    dataframe_tools.display_top_n_values(df)
    
    