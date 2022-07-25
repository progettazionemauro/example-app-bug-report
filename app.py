# Streamlit moduli streamlit
from curses.ascii import SP
from http import client
from tkinter import S
import streamlit as st
import pandas as pd



from pprint import pprint
from gsheetsdb import connect



# Create a connection object.
conn = connect()

# Get a list of all records

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.

st.title('Tabella documenti')

@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
dataframe = pd.DataFrame(run_query(f'SELECT * FROM "{sheet_url}"'))
#rowsData=run_query(f'SELECT * FROM "{sheet_url}" WHERE A="MDQ"') - NON FUNZIONA!!

# Print results (funzionante)
# for row in rows:
#   st.write(f"{row.DESCRIZIONE} ha il seguente titolo :{row.TITOLO}:")
#    st.markdown(f"{row.DESCRIZIONE} ha il seguente titolo :{row.TITOLO}:")

# Restituzione Dataframe
# df=pd.DataFrame
# df.style.set_table_styles([{'selector' : '', 'props' : [('border','10px solid yellow')]}])
st.dataframe(dataframe)
st.dataframe(dataframe.style.highlight_max(axis=0))
# st.dataframe(dataframe.set_option('max_rows', 7))
# st.dataframe(dataframe.set_option('max_columns', 3))
#st.dataframe(rowsData)






