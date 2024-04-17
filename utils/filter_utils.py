# utils/filter_utils.py

import streamlit as st
import pandas as pd

def filter_data(df):
    st.sidebar.header("Filters")
    selected_filters = st.sidebar.multiselect('Select filters:', df.columns.tolist())

    conditions = []
    for column in selected_filters:
        unique_values = pd.unique(df[column])
        selected_values = st.sidebar.multiselect(f"Values for {column}", unique_values)
        if selected_values:
            conditions.append(df[column].isin(selected_values))

    if conditions:
        combined_conditions = conditions[0]
        for condition in conditions[1:]:
            combined_conditions &= condition
        filtered_df = df[combined_conditions]
        return filtered_df
    return df
