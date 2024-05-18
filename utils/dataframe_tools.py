import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import search_utils

def display_dataframe(df):
    st.dataframe(df)
    
def dataframe_summary(df):
    st.markdown(f"Total Gallica records: **{df.shape[0]}** items  \nTotal columns: {df.shape[1]}") # This uses markdown to create a new line (Adding two spaces followed by \n at the end of the first line)
    # st.write(f"Total records: {df.shape[0]}")
    # st.write(f"Total columns: {df.shape[1]}")
    
    filtered_dates = df[df['date'].str.isdigit() & (df['date'].str.len() == 4)]['date']
    st.write(f"Document date range: {filtered_dates.min()}-{filtered_dates.max()}") # st.write(f"Document date range: {df['date'].min()} to {df['date'].max()}")

    st.write("Top 3 document languages:", df['language'].value_counts().head(3).to_string(header=False, index=True).replace('\n', ', '))

def show_column_counts(df):
    for column in df.columns:
        st.write(f"Counts for {column}:")
        st.write(df[column].value_counts())

def check_duplicates(df):
    if df.duplicated().any():
        st.write("There are duplicates in the dataset.")
    else:
        st.write("No duplicates found in the dataset.")

def dataframe_search(df):
    search_column = st.selectbox("Select column to search in:", df.columns)
    search_query = st.text_input("Enter search query:")
    if search_query:
        filtered_df = df[df[search_column].astype(str).str.contains(search_query, case=False, na=False)]
        st.write(f"Number of results: {len(filtered_df)}")
        st.dataframe(filtered_df)

def dataframe_toolbox(df):
    st.subheader('Dataframe Analysis Toolbox')
    dataframe_summary(df)
    show_column_counts(df)
    dataframe_search(df)
    
def display_top_n_values(df):
    # Allow the user to select the number of top items to display
    n = st.selectbox(
        "Select the number of top items to display:",
        options=[1, 2, 3, 4, 5, 10, 15, 20, 25, 50],
        index=2  # Default index for '5'
    )

    st.write(f"Displaying top {n} most frequent values for each column:")

    # Iterate through each column in the DataFrame
    for column in df.columns:
        st.subheader(f"Top {n} in '{column}'")
        # Calculate the frequency of each value in the column
        top_n = df[column].value_counts().head(n)
        # Display the frequency as a bar chart
        st.bar_chart(top_n)