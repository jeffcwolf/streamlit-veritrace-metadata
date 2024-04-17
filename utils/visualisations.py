# utils/visualisations.py

import streamlit as st
import matplotlib.pyplot as plt

def create_line_chart(df, x, y):
    fig, ax = plt.subplots()
    ax.plot(df[x], df[y], marker='o', linestyle='-')
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.grid(True)
    st.pyplot(fig)

def create_bar_chart(df, x, y):
    fig, ax = plt.subplots()
    ax.bar(df[x], df[y], color='blue')
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.grid(True)
    st.pyplot(fig)

def create_histogram(df, column):
    plt.hist(df[column].dropna(), bins=20, color='blue')
    plt.title(f'Histogram of {column}')
    st.pyplot(plt)

def common_graph(df, x_axis, y_axis):
    st.line_chart(df[[x_axis, y_axis]])