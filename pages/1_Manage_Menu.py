import streamlit as st
from auxillaries import *
import pandas as pd

def update_menu(groups_df, update_container, conn):
  with update_container:
    st.warning("Looks like you've made some changes. Finalise by clicking the button! Leave it be otherwise.")
    if st.button('Click here to update'):
      combined_df = pd.concat(groups_df.values(), axis=1)
      conn.update(
          worksheet="Sheet1",
          data=combined_df,
      )
      st.cache_data.clear()
      st.experimental_rerun()
    st.divider()

def display_current_menu(df, update_container, conn):
  groups_df = dict()
  for category, group_df in df.groupby('Category'):
    with st.expander(category):
      groups_df[category] = st.data_editor(group_df, on_change = update_menu, args = (groups_df, update_container, conn))
  return groups_df

def get_conn_df(conn):
  df = conn.read(ttl = 0)
  return df
      
if __name__ == "__main__":
  conn = initiate()
  df = get_conn_df(conn)
  st.subheader('Grand Chola - Menu')
  update_container = st.container()
  groups_df = display_current_menu(df, update_container, conn)
  st.dataframe(df)
