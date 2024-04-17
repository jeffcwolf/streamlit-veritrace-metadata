import streamlit as st
from utils import data_processing, download_utils, filter_utils, search_utils, templates, visualisations, dataframe_tools, catalog_utils
import os
import pandas as pd

def app():
    st.title('BSB Analysis')
    st.write("Welcome to the BSB analysis page.")    