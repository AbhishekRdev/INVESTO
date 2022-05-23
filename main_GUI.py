import yfinance as yf
import streamlit as st

from datetime import date,datetime,timedelta

from PIL import Image

from urllib.request import urlopen
#headers
# Pages = {"Crypto Forcasting": EDA_forcast}
# st.slidebar.title("Page View")
# selection = st.slidbar.radio("Applications",list(Pages.keys()))
# page = PAGES[selection]
# page.app()
def app():
    # st.title("Cryptocurrency_GUI")
    st.title("Cryptocurrency Price Viewer")
    st.header("Main Dashboard")
    # st.subheader("Room for more cryptocurrency")


    BTC = 'BTC-INR'
    ETH = 'ETH-INR'
    XRP = 'XRP-INR'
    BCH = 'BCH-INR'
    BTT = 'BTT-INR'

    #Accessing the data from the API
    BTC_data = yf.Ticker(BTC)
    ETH_data = yf.Ticker(ETH)
    XRP_data = yf.Ticker(XRP)
    BCH_data = yf.Ticker(BCH)
    BTT_data = yf.Ticker(BTT)

    # Fetching the past data from the yfinance API

    BTC_old = BTC_data.history(period = "max")
    ETH_old = ETH_data.history(period = "max")
    XRP_old = XRP_data.history(period = "max")
    BCH_old = BCH_data.history(period = "max")
    BTT_old = BTT_data.history(period = "max")

    # Crypto data for data frame
    end_date = date.today()
    end_date_str = end_date.strftime("%Y-%m-%d")
    start_date = end_date  - timedelta(days=2)
    start_date_str = start_date.strftime("%Y-%m-%d")

    st.info("Date updated :-"+end_date_str)



    BTC_dataframe = yf.download(BTC,start=start_date_str,end = end_date_str)
    ETH_dataframe = yf.download(ETH,start=start_date_str,end = end_date_str)
    XRP_dataframe = yf.download(XRP,start=start_date_str,end = end_date_str)
    BCH_dataframe = yf.download(BCH,start=start_date_str,end = end_date_str)
    BTT_dataframe = yf.download(BTT,start=start_date_str,end = end_date_str)

    #BITCOIN

    st.subheader("BITCOIN (in INR)")
    imgBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
    st.image(imgBTC)

    #Displaying the dataframe

    st.table(BTC_dataframe)
    #display infographics
    st.line_chart(BTC_old.Close)

    #ETHEREUM

    st.subheader("ETHEREUM (in INR)")
    imgETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
    st.image(imgETH)

    #Displaying the dataframe

    st.table(ETH_dataframe)
    #display infographics
    st.line_chart(ETH_old.Close)

    #RIPPLE

    st.subheader("RIPPLE (in INR)")
    imgXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
    st.image(imgXRP)

    #Displaying the dataframe

    st.table(XRP_dataframe)
    #display infographics
    st.line_chart(XRP_old.Close)

    #BITCOIN CASH

    st.subheader("BITCOIN CASH (in INR)")
    imgBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
    st.image(imgBCH)

    #Displaying the dataframe

    st.table(BCH_dataframe)
    #display infographics
    st.line_chart(BCH_old.Close)

    #BITTORRENT TOKEN

    st.subheader("BITTORRENT TOKEN (in INR)")
    imgBTT = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/16086.png'))
    st.image(imgBTT)

    #Displaying the dataframe

    st.table(BTT_dataframe)
    #display infographics
    st.line_chart(BTT_old.Close)

