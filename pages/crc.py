# pages/crc.py

import streamlit as st
from utils import data_processing, templates, visualisations, search_utils, filter_utils, download_utils

def app():
    df_crc = data_processing.load_crc_data()  # Assuming this function loads your data

    templates.common_header("CRC Analysis")
    templates.display_dataframe(df_crc)
    
    # Use search and filter utilities
    df_searched = search_utils.search_data(df_crc)
    df_filtered = filter_utils.filter_data(df_searched)

    # Display data and visualisation
    templates.display_dataframe(df_filtered)
    download_utils.display_download_button(df_crc, "CRC_data.csv", "Download CRC Data")
