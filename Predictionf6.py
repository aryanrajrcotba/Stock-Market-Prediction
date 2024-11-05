import streamlit as st #Creating the data visualization tool
from datetime import date 
import numpy as np
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd


#Creating the start date
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

#Starting the web app

#Giving the title
st.title("Stock Predicition App")

stocks = ("AAPL", "GOOG", "MSFT", "GME", "NVDA", "INTC", "TSLA", "DELL", "AMZN", "BTC-USD", "DOGE-USD", "ESTC")
#Selecting which stock we want to predict
selected_stock = st.selectbox("Select DataSet for Predicition", stocks)

#df = pd.read_csv('C:/Users/aryan/Downloads/archive/SBIN.csv')

#Selecting the years of predicition
n_years = st.slider("Years of Predicition: ", 1, 4)
period = n_years * 365

#To cache the downloaded data
#@st.cache_data
#Function to Load Data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data 

data_load_state = st.text("Load Data ...")
data = load_data(selected_stock)
data_load_state.text("Loading data.... Done!!")

#data = pd.read_csv('C:/Users/shiva/Downloads/archive/TATASTEEL.csv')
#data.reset_index(inplace=True)

#Analyis the raw data
st.subheader("Raw Data")
st.write(data.tail())

#Plotting the raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Stock_Open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock_Close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

#Forecasting
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})


#Creating a forecasting model
m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader("Forecasted Data")
st.write(forecast.tail())

#Plotting the forecast data
st.write('Forecast Data')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write('Forecast Componenets')
fig2 = m.plot_components(forecast)
st.write(fig2)
