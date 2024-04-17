# pages/drc.py

import streamlit as st
from utils import data_processing, download_utils, filter_utils, search_utils, templates, visualisations
import os
import pandas as pd

def app():
    st.title('DRC Analysis')
    st.write("Welcome to the DRC analysis page.")
    
    df_eebo = data_processing.load_eebo_data()
    df_gallica = data_processing.load_gallica_data()
    df_bsb = data_processing.load_bsb_data()

    # EEBO Metadata
    templates.common_header("EEBO Analysis")
    st.title('EEBO Metadata')
    templates.display_dataframe(df_eebo)
    
    # Use search and filter utilities
    st.title('Search and Filter')
    df_searched = search_utils.search_data(df_eebo)
    df_filtered = filter_utils.filter_data(df_searched)

    # Display data and visualisation
    # templates.display_dataframe(df_filtered)
    download_utils.display_download_button(df_eebo, "eebo.csv", "Download EEBO Data")
    
    # GALLICA Metadata
    templates.common_header("Gallica Analysis")
    templates.display_dataframe(df_gallica)
    
    # Use search and filter utilities
    df_searched = search_utils.search_data(df_gallica)
    df_filtered = filter_utils.filter_data(df_searched)

    # Display data and visualisation
    templates.display_dataframe(df_filtered)
    download_utils.display_download_button(df_gallica, "gallica.csv", "Download Gallica Data")