import streamlit as st
from auxillaries import *
from datetime import datetime, timedelta
import pytz

def show_reservations(conn):
  date = st.date_input("📅 Reservation Date", value="default_value_today" , format="DD/MM/YYYY").strftime('%d/%m/%Y')
  if date in worksheet_names(conn):
    df = read_worksheet(conn, date).dropna(how = "all")
    if len(df) > 0:
      # Reshape the dataframe
      melted_df = pd.melt(df, id_vars=['Name', 'Group size', 'Number'], var_name='Time', value_name='Availability')
      
      # Convert 'Time' column to datetime format
      melted_df['Time'] = pd.to_datetime(melted_df['Time'].str.replace(' hrs', ''), format='%H:%M')
      
      # Filter out rows where availability is not null
      result_df = melted_df.dropna(subset=['Availability'])
      
      # Group by Name, Group size, and Number, and select the row with the minimum availability time
      result_df = result_df.groupby(['Name', 'Group size', 'Number']).apply(lambda x: x.loc[x['Time'].idxmin()]).reset_index(drop=True)
      result_df['Time'] = pd.to_datetime(result_df['Time']).dt.strftime('%H:%M')
      result_df = result_df[['Name', 'Group size', 'Number', 'Time']]
      
      st.dataframe(result_df,
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
