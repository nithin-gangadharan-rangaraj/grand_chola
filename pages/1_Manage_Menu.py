import streamlit as st
from auxillaries import *

def display_current_menu(df):
  st.subheader('Grand Chola - Menu')
  groups_df = dict()
  for category, group_df in df.groupby('Category'):
    with st.expander(category):
      groups_df[category] = st.data_editor(group_df)
  return groups_df
      
if __name__ == "__main__":
  df = initiate()
  groups_df = display_current_menu(df)
