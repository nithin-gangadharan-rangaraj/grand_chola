import streamlit as st
from auxillaries import *

def display_current_menu(df):
  st.subheader('Current Menu')
  for category, group_df in df.groupby('Category'):
    with st.expander(category):
      st.dataframe(group_df[['Item','Price (AUD)','Description']])
      
if __name__ == "__main__":
  df = initiate()
  display_current_menu(df)
