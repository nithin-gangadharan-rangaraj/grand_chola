import streamlit as st
from auxillaries import *

style = '''
    <style>
        header {visibility: hidden;}
        MainMenu {visibility: hidden;}
        .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
    </style>
'''

def display_menu(df):
  for category, group_df in df.groupby('Category'):
    st.subheader(f"{category.upper()}:", divider = 'orange')
    for idx, row in group_df.iterrows():
      st.write(f"**{row['Item'].capitalize()} - {row['Price (AUD)']}**")
      st.write(f"{row['Description']}")
    st.divider()

if __name__ == "__main__":
  df = initiate()
  display_menu(df)
