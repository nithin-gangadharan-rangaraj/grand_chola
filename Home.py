import streamlit as st
from auxillaries import *

st.set_page_config(page_title="Grand Chola")

st.config(auto_pages=False)

st.add_pages(
  {
  "Reservations": "pages/1_Reservation.py",
  }
)

if __name__ == "__main__":
  # st.image('chola.png', width = 500)
  st.header('Welcome', divider = 'orange')
  st.write('Click the side bar on the top left corner to start.')
