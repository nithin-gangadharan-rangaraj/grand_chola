import streamlit as st
from auxillaries import *

st.set_page_config(page_title="Grand Chola - Menu",layout='wide')


style = '''
    <style>
        header {visibility: hidden;}
        MainMenu {visibility: hidden;}
        .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                }
    </style>
'''
st.markdown(style, unsafe_allow_html=True)

def display_menu(df):
  for category, group_df in df.groupby('Category'):
    st.subheader(f"{category.upper()}:", divider = 'orange')
    for idx, row in group_df.iterrows():
      st.write(f"**{row['Item'].capitalize()} - {row['Price (AUD)']}**")
      st.write(f"{row['Description']}")
    st.divider()

def display_logo():
  st.title('GRAND CHOLA')
  st.write('**Discover :orange[authentic Indian cuisine], reimagined.**')
  # st.image('chola.png', width = 200)

if __name__ == "__main__":
  df = initiate()
  display_logo()
  display_menu(df)
