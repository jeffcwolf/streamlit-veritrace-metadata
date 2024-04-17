import streamlit as st
import base64
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt

def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.

    Args:
    - object_to_download (DataFrame or Figure): The object to be downloaded.
    - download_filename (str): The filename under which the object will be downloaded.
    - download_link_text (str): The text of the download link.

    Returns:
    - str: The HTML anchor tag to download the object.
    """
    if isinstance(object_to_download, pd.DataFrame):
        towrite = BytesIO()
        object_to_download.to_csv(towrite, encoding='utf-8', index=False, sep=',')
        towrite.seek(0)
        b64 = base64.b64encode(towrite.read()).decode()
    else:  # Assume matplotlib figure for simplicity
        towrite = BytesIO()
        object_to_download.savefig(towrite, format='png')
        towrite.seek(0)
        b64 = base64.b64encode(towrite.read()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

def display_download_button(df_or_fig, filename, button_text):
    """
    Display a download button in the Streamlit app for the given DataFrame or figure.

    Args:
    - df_or_fig (DataFrame or Figure): The object to be downloaded.
    - filename (str): The filename under which the object will be downloaded.
    - button_text (str): The text displayed on the download button.
    """
    if st.button(button_text):
        html = download_link(df_or_fig, filename, f"Click here to download {filename}")
        st.markdown(html, unsafe_allow_html=True)
