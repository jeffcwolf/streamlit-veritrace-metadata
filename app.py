import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px  # Importing Plotly for interactive plots
import seaborn as sns
import os

from pages import home, crc, drc, gallica, eebo, bsb


# app.py

# Set page config to wide mode
st.set_page_config(layout="wide")

# Dictionary of pages
pages = {
    "CRC": crc.app,
    "DRC": drc.app,
    "Gallica": gallica.app,
    "EEBO": eebo.app,
    "BSBS": bsb.app
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Call the app function based on selection
page = pages[selection]
page()

if st.button('Clear cache and rerun'):
    st.cache_data.clear()
    st.experimental_rerun()

# SEARCHING

# # Create a column selector for the search
# search_column = st.selectbox("Select column to search in:", df_eebo.columns.tolist())

# # Create a text input for the search query
# search_query = st.text_input("Enter search query:")

# # Perform the search and filter the dataframe if a query is entered
# if search_query:
#     # Filter dataframe based on the search query and selected column
#     filtered_df = df_eebo[df_eebo[search_column].astype(str).str.contains(search_query, case=False, na=False)]

#     # Display summary statistics
#     st.subheader('Search Summary')
#     st.write(f"Number of results: {len(filtered_df)}")

#     # Display the filtered dataframe if results are found
#     if not filtered_df.empty:
#         st.subheader('Search Results')
#         st.dataframe(filtered_df, width=None, height=300)
#     else:
#         st.write("No results found.")
# else:
#     st.write("Please enter a query to display results.")

# # ADVANCED FILTERING

# # Adding multiple filters
# st.sidebar.header("Filters")
# unique_columns = df_eebo.columns.tolist()

# # Allow users to select multiple filters
# selected_filters = st.sidebar.multiselect('Select filters:', unique_columns)

# # For each selected filter, allow users to specify the values they are interested in
# conditions = []
# for column in selected_filters:
#     unique_values = pd.unique(df_eebo[column])
#     selected_values = st.sidebar.multiselect(f"Values for {column}", unique_values)
#     if selected_values:
#         conditions.append(df_eebo[column].isin(selected_values))

# # Combine all conditions
# if conditions:
#     combined_conditions = conditions[0]
#     for condition in conditions[1:]:
#         combined_conditions = combined_conditions & condition
#     filtered_df = df_eebo[combined_conditions]
# else:
#     filtered_df = df_eebo

# # Display the filtered dataframe
# st.dataframe(filtered_df)

# # VISUALISATIONS

# # Visualize data - Histogram
# plot_column = st.selectbox('Select column to plot:', df_eebo.columns.tolist())
# if st.button('Generate histogram'):
#     plt.hist(df_eebo[plot_column].dropna(), bins=20, color='blue')
#     plt.title(f'Histogram of {plot_column}')
#     plt.xlabel(plot_column)
#     plt.ylabel('Frequency')
#     st.pyplot(plt)
    
# # Interactive plotting with Plotly
# st.header("Interactive Plots")
# plot_column = st.selectbox('Choose a column for Plotly visualization:', df_eebo.columns.tolist(), index=0)
# if st.button('Generate Plotly plot'):
#     fig = px.histogram(df_eebo, x=plot_column)
#     st.plotly_chart(fig) 

# # Static plotting with Seaborn
# st.header("Static Plots with Seaborn")
# plot_seaborn_column = st.selectbox('Choose a column for Seaborn visualization:', df_eebo.columns.tolist(), index=0)
# plot_kind = st.selectbox('Select kind of plot:', ['boxplot', 'violin', 'countplot'])
# if st.button('Generate Seaborn plot'):
#     plt.figure(figsize=(10, 6))
#     if plot_kind == 'boxplot':
#         sns.boxplot(x=df_eebo[plot_seaborn_column])
#     elif plot_kind == 'violin':
#         sns.violinplot(x=df_eebo[plot_seaborn_column])
#     elif plot_kind == 'countplot':
#         sns.countplot(x=df_eebo[plot_seaborn_column])
#     plt.title(f'Seaborn {plot_kind} of {plot_seaborn_column}')
#     st.pyplot(plt) 
