import streamlit as st
import yfinance as yf
import urllib.request
import urllib.error

st.title("Stock Price Checker")

ticker = st.text_input("Enter a stock ticker:", "AAPL")

try:
    data = yf.Ticker(ticker).history(period="1d")
    if not data.empty:
        st.write(f"**{ticker}** current price: ${data['Close'][0]:.2f}")
    else:
        st.write("No data found for that ticker.")

except urllib.error.HTTPError as err:
    st.write(f"HTTP error: {err.code}")
except urllib.error.URLError as err:
    st.write(f"URL error: {err.reason}")
except Exception as err:
    st.write(f"Unexpected error: {err}")