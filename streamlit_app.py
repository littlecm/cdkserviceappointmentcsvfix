import streamlit as st
import pandas as pd

def sum_numbers_in_cell(cell):
    if pd.isna(cell):
        return 0
    return sum(float(num) for num in str(cell).split())

def process_dataframe(uploaded_file):
    df = pd.read_csv(uploaded_file)

    df['sold_hours_total'] = df['sold_hours'].apply(sum_numbers_in_cell)
    df['parts_total'] = df['parts'].apply(sum_numbers_in_cell)

    df.drop(['sold_hours', 'parts'], axis=1, inplace=True)

    return df

st.title('CSV File Processor')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    st.write("Original Data")
    original_df = pd.read_csv(uploaded_file)
    st.write(original_df)

    processed_df = process_dataframe(uploaded_file)
    st.write("Processed Data")
    st.write(processed_df)
