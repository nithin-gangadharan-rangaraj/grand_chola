import streamlit as st
from auxillaries import *
from datetime import datetime, timedelta
import pytz

def show_reservations(conn):
  date = st.date_input("📅 Reservation Date", value="default_value_today" , format="DD/MM/YYYY").strftime('%d/%m/%Y')
  if date in worksheet_names(conn):
    df = read_worksheet(conn, date).dropna(how = "all")
    if len(df) > 0:
      st.dataframe(df,
                  column_config={
                                  "Number": st.column_config.NumberColumn(
                                      format="%d",
                                  )
                                })   
    else:
      st.error('No reservations for the selected date')
  else:
    st.error('No reservations for the selected date')


if __name__ == "__main__":
  st.title("Reservations")
  conn = initiate()
  show_reservations(conn)
