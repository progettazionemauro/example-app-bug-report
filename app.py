# Streamlit moduli streamlit
from curses.ascii import SP
from http import client
import streamlit as st
import pandas as pd



from pprint import pprint
# from gsheetsdb import connect

df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))





