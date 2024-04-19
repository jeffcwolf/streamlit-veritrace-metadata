import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import search_utils

def interactive_date_plot(df, date_column):
    st.subheader("Publication Trend Over Time")

    # Convert date column to string and filter out entries that are not 4-digit years
    df = df[df[date_column].astype(str).str.match(r'^\d{4}$')]
    
    # Convert date column to integer format for year comparison
    df[date_column] = pd.to_numeric(df[date_column], errors='coerce')
    
    # Drop rows where dates could not be converted (e.g., invalid dates)
    df = df.dropna(subset=[date_column])

    # Check if there are any dates to process
    if not df.empty:
        # Convert years to integers for handling
        df[date_column] = df[date_column].astype(int)

        # Create a slider to select the date range, convert the range to integers
        min_year, max_year = int(df[date_column].min()), int(df[date_column].max())
        selected_years = st.slider("Select Date Range", 
                                   min_value=min_year,
                                   max_value=max_year,
                                   value=(min_year, max_year))

        # Filter the dataframe based on the selected date range
        filtered_df = df[(df[date_column] >= selected_years[0]) & (df[date_column] <= selected_years[1])]

        # Plotting the data
        fig, ax = plt.subplots()
        filtered_df.groupby([date_column]).size().plot(kind='line', ax=ax)
        st.pyplot(fig)
    else:
        st.write("No valid data available for the selected date column.")

# def interactive_date_plot(df, date_column):
#     st.subheader("Publication Trend Over Time")
#     df[date_column] = pd.to_datetime(df[date_column])
#     min_date, max_date = st.slider("Select Date Range", 
#     min_value=df[date_column].min(),
#     max_value=df[date_column].max(),
#     value=(df[date_column].min(), df[date_column].max()))
#     filtered_df = df[(df[date_column] >= min_date) & (df[date_column] <= max_date)]
#     fig, ax = plt.subplots()
#     filtered_df.groupby(filtered_df[date_column].dt.year).size().plot(kind='line', ax=ax)
#     st.pyplot(fig)

def top_n_authors(df, author_column, n=5):
    st.subheader(f"Top {n} Authors by Publication")
    top_authors = df[author_column].value_counts().head(n)
    st.bar_chart(top_authors)

def top_hits_by_author_and_title_gallica(df):
    # Group by 'creator' and 'title', and get the size of each group
    aggregated_data = df.groupby(['creator', 'title']).size().reset_index(name='counts')
    
    # Get the top 5 rows with the largest counts
    top_data = aggregated_data.nlargest(5, 'counts')
    
    # Create a new column 'creator_title' that combines 'creator' and 'title'
    top_data['creator_title'] = top_data['creator'] + ' - ' + top_data['title']
    
    # Create a plot
    fig, ax = plt.subplots(figsize=(10, 8))
    # Plot data using the new 'creator_title' column for the x-axis
    top_data.plot(kind='bar', x='creator_title', y='counts', ax=ax)
    
    # Rotate x-tick labels for better readability
    plt.xticks(rotation=45, ha='right')
    
    # Display the plot in Streamlit
    st.pyplot(fig)

def common_publishers_and_places(df):
    publisher_counts = df['publisher'].value_counts().nlargest(10)
    place_counts = df['place'].value_counts().nlargest(10)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    publisher_counts.plot(kind='barh', ax=ax1, title='Top 10 Publishers')
    place_counts.plot(kind='barh', ax=ax2, title='Top 10 Publication Places')
    st.pyplot(fig)

def search_by_author_and_term(df, author, term):
    return search_utils.advanced_search(df, ['author'], f"{author} & {term}")

def search_by_title_and_term(df, title, term):
    return search_utils.advanced_search(df, ['title'], f"{title} & {term}")

def plot_language_distribution(df, column_name='language'):
    # Reduce figure size to 60% of the original size
    plt.figure(figsize=(6, 3.6))  # 60% of (10, 6)
    ax = sns.countplot(x=column_name, data=df, order=df[column_name].value_counts().index)
    ax.set_title('Language Distribution')
    ax.set_xlabel('Language')
    ax.set_ylabel('Number of Records')
    plt.xticks(rotation=45, ha='right')  # Rotate labels for better readability if needed

    # Add value counts above the bars
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points')

    st.pyplot(plt)