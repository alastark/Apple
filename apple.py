import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def apple():
    st.title('Приложение для отображения котировок компании Apple')
    st.write("Введите даты начала и конца периода котировок:")
    start_date = st.date_input('Дата начала', value=pd.to_datetime('2020-01-01'))
    end_date = st.date_input('Дата конца', value=pd.to_datetime('2020-12-31'))
    data = yf.download('AAPL', start=start_date, end=end_date)
    data = data.reset_index()
    fig, ax = plt.subplots()
    ax.plot(data['Date'], data['Close'])
    plt.xticks(rotation=45)
    ax.set(xlabel='Дата', ylabel='Цена закрытия', title='Котировки компании Apple')
    plt.grid()
    st.pyplot(fig)

if __name__ == '__main__':
    apple()
