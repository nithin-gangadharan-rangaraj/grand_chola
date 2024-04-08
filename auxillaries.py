
import streamlit as st
from streamlit_gsheets import GSheetsConnection

def initiate():
  # Create a connection object.
  conn = st.connection('gsheets', type=GSheetsConnection)
  
  df = conn.read(Spreadsheet = st.secrets['sheet_name'],
                 worksheet="Sheet1",
                 ttl="0")
  return df

# from google.oauth2 import service_account
# import streamlit as st
# import gspread
# import pandas as pd

  
# def initiate():
#   if 'gsheet' in st.session_state:
#       gsheet = st.session_state['gsheet']
#   else:
#       # Load service account credential
#       service_acc = st.secrets["gcp_service_account"]
      
          
#       credentials = service_account.Credentials.from_service_account_info(
#       service_acc,
#       scopes=[
#           "https://www.googleapis.com/auth/spreadsheets",
#           "https://www.googleapis.com/auth/drive"
#       ],
#       )
  
#       # Authorize gspread client
#       gs = gspread.authorize(credentials)
#       st.write(st.secrets['sheet_name'])
#       gsheet = gs.open(st.secrets['sheet_name'])
#       st.session_state['gsheet'] = gsheet
#   return gsheet

