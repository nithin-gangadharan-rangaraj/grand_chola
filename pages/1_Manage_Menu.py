import streamlit as st
from auxillaries import *
import pandas as pd

def update_menu(groups_df, update_container):
  with update_container:
    st.warning("Looks like you've made some changes. Finalise by clicking the button! Leave it be otherwise.")
    if st.button('Click here to update'):
      combined_df = pd.concat(groups_df.values(), axis=1)
      st.dataframe(combined_df)
    st.divider()

def display_current_menu(df, update_container):
  groups_df = dict()
  for category, group_df in df.groupby('Category'):
    with st.expander(category):
      groups_df[category] = st.data_editor(group_df, on_change = update_menu, args = (groups_df, update_container))
  return groups_df
      
if __name__ == "__main__":
  df = initiate()
  st.subheader('Grand Chola - Menu')
  update_container = st.container()
  groups_df = display_current_menu(df, update_container)
  combined_df = pd.concat(groups_df.values(), axis=1)
  st.dataframe(combined_df)
