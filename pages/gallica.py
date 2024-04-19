import streamlit as st
from utils import data_processing, download_utils, filter_utils, search_utils, templates, visualisations, dataframe_tools, catalog_utils
import pandas as pd
import os


def app():
    st.title('Gallica Analysis Metadata (Beta)')
    st.write("Welcome to the Gallica data source analysis page. NOTE: All Metadata is raw and has not been cleaned or processed.")    
    
    # Load the data
    df = data_processing.load_gallica_data()

    # Print general information about the dataset
    st.write("Gallica is the digital library of the Bibliothèque nationale de France and its partners. On-line since 1997, it adds thousands of new items every week and now offers access to several million documents.")
    st.write("The metadata we use was downloaded from the Gallica website.")
    
    # Add dataframe tools
    dataframe_tools.dataframe_summary(df)
    
    # Display the data
    if df is not None and not df.empty:
        templates.display_dataframe(df)
    else:
        st.write("No data available.")
    
    # SEARCH
    st.markdown("## Search Data  \nSearch results appear below the search bar.")
    df_searched = search_utils.search_data(df)
    if df_searched is not None:
        # Display the number of results found
        st.write(f"Total results: {len(df_searched)}")
        # Display the dataframe using a custom function or directly
        templates.display_dataframe(df_searched)
    
    #FILTERING

    # Adding multiple filters
    st.sidebar.header("Filters")
    unique_columns = df.columns.tolist()

    # Allow users to select multiple filters
    selected_filters = st.sidebar.multiselect('Select filters:', unique_columns)

    # For each selected filter, allow users to specify the values they are interested in
    conditions = []
    for column in selected_filters:
        unique_values = pd.unique(df[column])
        selected_values = st.sidebar.multiselect(f"Values for {column}", unique_values)
        if selected_values:
            conditions.append(df[column].isin(selected_values))

    # Combine all conditions
    if conditions:
        combined_conditions = conditions[0]
        for condition in conditions[1:]:
            combined_conditions = combined_conditions & condition
        df_filtered = df[combined_conditions]
    else:
        df_filtered = df

    # Display the filtered dataframe
    st.markdown("## Filtered Data  \nFiltered results appear below the filter bar.")
    if df_searched is not None:
        # Display the number of results found
        st.write(f"Total results: {len(df_filtered)}")
        # Display the dataframe using a custom function or directly
        templates.display_dataframe(df_filtered)
    
    # ANALYTICS
    st.markdown("## Analytics  \nDisplaying some basic analytics on the data.")
    n = 5
    
    st.subheader(f"Top {n} Creators by Record Count")
    top_authors = df['creator'].value_counts().head(n)
    st.write(top_authors)
    
    st.subheader(f"Top {n} Publishers by Record Count")
    top_publishers = df['publisher'].value_counts().head(n)
    st.write(top_publishers)
    
    st.subheader(f"Top {n} Dates by Record Count")
    top_dates = df['date'].value_counts().head(n)
    st.write(top_dates)
    
    # GRAPHS & VISUALISATIONS
    st.markdown("### Graphs & Visualisations")
    
    if st.button('Show Language Distribution'):
        catalog_utils.plot_language_distribution(df, 'language')
        
    if st.button('Interactive Date Plot'):
        catalog_utils.interactive_date_plot(df, 'date')
    
    # Top hits
    # catalog_utils.top_hits_by_author_and_title_gallica(df)
    
    # Display top n values for each column
    # dataframe_tools.display_top_n_values(df)
    
    