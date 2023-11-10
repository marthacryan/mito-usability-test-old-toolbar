
import streamlit as st
import pandas as pd 
from mitosheet.streamlit.v1 import spreadsheet
from mitosheet.extensions.v1 import ColumnHeader

st.set_page_config(layout="wide")

analysis = spreadsheet(
    df_names=['df'],
    import_folder='data',
    return_type='analysis'
)
