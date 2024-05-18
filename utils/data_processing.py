'''

1. Data Loading
Functions to load data from various sources such as CSV files, databases, APIs, or even real-time data streams.
Handling different data formats and ensuring they are correctly parsed into a usable form, like pandas DataFrames.
2. Data Cleaning
Functions to clean data, which could include handling missing values, removing duplicates, or correcting data errors.
Normalizing or standardizing data, such as adjusting date formats, converting text to lowercase, or mapping values to consistent categories.
3. Data Transformation
Transforming data to be suitable for analysis, such as pivoting tables, merging datasets, or creating new calculated columns.
Aggregating data, for instance, summing up sales figures by region or calculating average values.
4. Feature Engineering
Creating new features from existing data to improve the performance of analytical models or to enhance visualizations.
Techniques could include extracting parts of dates (like day of week from a date), binning continuous data into categories, or creating interaction terms in dataset.
5. Data Filtering
Functions to subset data based on certain criteria, useful for creating specific views or feeding into particular visualizations or analyses.
Example includes filtering a dataset for a specific time period, a specific user demographic, or products of interest.
6. Data Summarization
Generating summary statistics that describe data sets, useful for initial explorations and for display on dashboards.
Typical summarizations include computing means, medians, modes, or more complex statistical measures.
7. Data Caching
Implementing caching mechanisms to optimize performance, especially useful when dealing with large datasets or complex transformations that are computationally expensive.



'''
import pandas as pd
import os

# Load the general dataframes from external files stored on sync.com

# Gallica
gallica_file_path = 'data/vgallica_metadata_original.json'
df_gallica = pd.read_json(gallica_file_path, lines=True)

# EEBO

# BSB

# CRC
# crc_file_path = 'data/crc.csv'
# df_crc = pd.read_csv(crc_file_path, low_memory=False)

def load_crc_data():
    return pd.read_csv('data/crc.csv', low_memory=False)

def load_eebo_data():
    return pd.read_csv('data/veebo_metadata_original_final_short.csv', low_memory=False)
# def load_gallica_data_all():
#     file_path = 'data/vgallica_metadata_original.json'
#     if os.path.exists(file_path):
#         try:
#             df_gallica = pd.read_json(file_path, lines=True)
#             print(f"Data loaded successfully with {df.shape[0]} records.")
#             return df_gallica
#         except ValueError as e:
#             print(f"Error reading the JSON file: {e}")
#             return pd.DataFrame()  # Return an empty DataFrame on error
#     else:
#         print(f"File does not exist at path: {file_path}")
#         return pd.DataFrame()  # Return an empty DataFrame if file does not exist

def load_gallica_data():
    # Return a subset of the data for demonstration purposes
    gallica_columns_to_analyse = ['date', 'title', 'creator', 'contributor', 'publisher', 'language',
    'description', 'format', 'type', 'identifier', 'source', 'OCR_Quality', 'Provenance', 'subject', 'Full ARK ID','filename', 'file size (MB)']
    
    gallica_columns_to_analyse_small = ['date', 'title', 'creator', 'contributor', 'publisher', 'language',
    'description', 'format', 'source', 'OCR_Quality', 'subject', 'file size (MB)']
    
    df_gallica_sub = df_gallica[gallica_columns_to_analyse]
    df_gallica_sub_small = df_gallica[gallica_columns_to_analyse_small]
    
    return df_gallica_sub_small

def load_bsb_data():
    return pd.DataFrame()

