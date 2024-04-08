import streamlit as st
from auxillaries import *

def update_menu(groups_df, update_container):
  update_container.warning("Looks like you've updated your menu. Finalise by clicking the button!")
  update_container.button('Click here to update')

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
  
