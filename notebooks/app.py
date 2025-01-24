import streamlit as st
import pandas as pd

# Load the precomputed Lookalike data
lookalike_df = pd.read_csv(r"C:\Users\mistr\Desktop\zeotap\output\Meet_Mistry_Lookalike.csv")

# Streamlit app layout
st.title("Customer Lookalike Finder")
st.write("Find top 3 lookalike customers based on your input.")

# Input from the user
input_customer_id = st.text_input("Enter a Customer ID:")

# Show lookalikes
if st.button("Find Lookalikes"):
    if input_customer_id in lookalike_df['CustomerID'].values:
        lookalikes = lookalike_df.loc[lookalike_df['CustomerID'] == input_customer_id, 'Lookalikes'].values[0]
        st.write(f"Top 3 lookalike customers for **{input_customer_id}**:")
        for lookalike in lookalikes.split(', '):
            st.write(lookalike)
    else:
        st.error("Customer ID not found!")
