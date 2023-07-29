import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components

# st.set_page_config(
#     layout="wide"
# )

def main():
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)

        pyg_html = pyg.walk(df, return_html=True)
        components.html(pyg_html, height=900, scrolling=True)


if __name__ == "__main__":
    main()




