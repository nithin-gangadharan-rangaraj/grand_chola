import streamlit as st
from auxillaries import *

def display_menu(df):
  for category, group_df in df.groupby('Category'):
    st.subheader(f"{category.upper()}:", divider = 'orange')
    for idx, row in group_df.iterrows():
      st.write(f"**{row['Item'].capitalize()}**")
      st.write(f"Price: {row['Price (AUD)']}")
      st.write(f"{row['Description']}")
    st.divider()

if __name__ == "__main__":
  df = initiate()
  display_menu(df)
