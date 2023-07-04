import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st

start = '2009-12-31'
end = '2023-06-20'

st.title('Stock Trend Model')

user_input = st.text_input('Enter Sttock Ticker', 'AAPL')
df = data.DataReader('TQQQ', 'stooq', start, end)


#Describing the Data
st.subheader('Data from 2010 - 2019')
st.write(df.describe())

