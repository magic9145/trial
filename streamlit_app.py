pip install yfinance
pip install plotly
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
import streamlit as st

st.title('Live Stock Price')

stock = st.text_input("Please enter stock ticker: ")
data = yf.download(tickers=stock, period='1d', interval='1m')

fig = go.Figure()

fig.add_trace(go.Candlestick(x=data.index,
                            open=data['Open'],
                            high=data['High'],
                            low=data['Low'],
                            close=data['Close'], name='market data'))

fig.update_layout(
    title='Stock live share price',
    yaxis_title='Stock Price($USD)')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list((
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=3, label="3h", step="hour", stepmode="backward"),
            dict(step="all")
        ))
    )
)
st.subheader("Live share price graph")
st.plotly_chart(fig)
