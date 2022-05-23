
import streamlit as st
from datetime import date
from PIL import Image
import time
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

def app():
    START_date = "2015-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    #title for the app
    st.title("Stock Prediction App💵💹💸")

    stocks = ("QCOM","FB","MSFT","NVDA","AAPL","GOOG")
    #selection box
    sel_stock = st.sidebar.selectbox("Select the stock for prediction",stocks)
    #period_years = st.slider("Years of prediction:",1,5)
    period_years  = st.sidebar.slider("Years of prediction:",1,10)
    period = period_years*365

    @st.cache()
    def load_stock_data(ticker):
        
        data = yf.download(ticker,START_date,TODAY)
        data.reset_index(inplace = True)
        return data
    #image of Company
    for i in stocks:
            if(sel_stock == i):
                img = "".join([sel_stock,".png"])
                st.image("img_src/"+img)

    load = st.error("Please Wait!!.Loading Data...........")
    time.sleep(2)
    load.write(" ")
    data = load_stock_data(sel_stock)
    done = st.success("Loading Data........ DONE!!")
    st.write("\n\n")
    st.subheader("Original Data(RAW DATA)")
    st.write(data.tail())
    
    time.sleep(3)
    done.write("")
    
    # load_data_txt.text("")
    # st.write("\n\n")
    # st.subheader("Original Data(RAW DATA)")
    # st.write(data.tail())

    def plot_data_raw():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'],name = 'stock_open'))
        fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name = 'stock_close'))
        fig.layout.update(title_text = "Time Series Data",xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_data_raw()

    #forcasting data (using prophet)
    run_once = False
    st.subheader("Filtered Rows")
    sel_indices = st.sidebar.multiselect("Select Rows:-",data.index)
    st.table(data.loc[sel_indices])
    def train_model():

        df_train = data[['Date','Close']]
        df_train = df_train.rename(columns={"Date":"ds","Close":"y"})
        return df_train
    while(not run_once):
        m = Prophet()
        m.fit(train_model())
        run_once = True
    

    fut = m.make_future_dataframe(periods=period)
    forcast = m.predict(fut)


    st.subheader("Forcast DATA")
    st.write(forcast.tail())

    st.subheader("FORCASTED DATA PLOT")
    fig1 = plot_plotly(m,forcast)
    st.plotly_chart(fig1)

    st.write("COMPONENTS")
    fig_2 = m.plot_components(forcast)
    st.write(fig_2)




