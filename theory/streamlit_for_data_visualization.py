# To run this script:
# Install Streamlit if you haven't already: pip install streamlit
# In your terminal, run: streamlit run [path of the script]

import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import plotly.express as px

# Set the title of the app
st.title('Streamlit Tutorial:  Data Visualization')

# Introduction
st.markdown("""
## Introduction

We'll explore how to use Streamlit to build interactive web applications for data visualization. We'll cover:
- Displaying static and interactive tables
- Creating static and dynamic graphs
- Adding widgets for user interaction
- An  example with financial data visualization
""")

# ---------------------------------------
# Section 1: Displaying Data Tables
# ---------------------------------------
st.header('1. Displaying Data Tables')

# Create a random DataFrame to plot & display data
@st.cache_data
def create_sample_data():
    """Generates a sample DataFrame."""
    np.random.seed()
    data = pd.DataFrame({
        'Time': pd.date_range(start='2021-01-01', periods=100, freq='D'),
        'Asset_A': np.random.randn(100).cumsum() + 100,
        'Asset_B': np.random.randn(100).cumsum() + 100,
        'Asset_C': np.random.randn(100).cumsum() + 100,
    })
    return data

data = create_sample_data()

# Display the DataFrame as a static table
st.subheader('Static Table')
st.write('Here is a static table of our sample data:')
st.table(data.head())

# Display the DataFrame as an interactive table
st.subheader('Interactive Table')
st.write('Below is an interactive table that you can sort and scroll:')
st.dataframe(data.head())

# Highlight maximum values in the DataFrame
st.subheader('Highlighted Table')
st.write('This table highlights the maximum value in each column:')
st.dataframe(data.style.highlight_max(axis=0))

# ---------------------------------------
# Section 2: Displaying Static Graphs
# ---------------------------------------
st.header('2. Displaying Static Graphs')

# Line Chart
st.subheader('basic Line Chart')
st.write('A simple line chart of Asset_A over time:')
st.line_chart(data.set_index('Time')['Asset_A'])

"""
alternative way to do it if you want to adjust the y-axis to the value display :
"""

# Set dynamic y-axis limits
y_min = data['Asset_A'].min() - 5
y_max = data['Asset_A'].max() + 5

# Create an Altair chart
chart = alt.Chart(data).mark_line().encode(
    x='Time:T',
    y=alt.Y('Asset_A:Q', scale=alt.Scale(domain=[y_min, y_max]))  # Dynamic y-axis limits
).properties(
    width=700,  # You can adjust the width or remove this for auto-sizing
    height=400  # Adjust height
)

# Streamlit Header and Chart
st.subheader('Line Chart')
st.write('A simple line chart of Asset_A over time:')
st.altair_chart(chart, use_container_width=True)


# Area Chart
st.subheader('Area Chart')
st.write('An area chart of all assets:')
st.area_chart(data.set_index('Time'))

# Bar Chart
st.subheader('Bar Chart')
st.write('A bar chart of the last 10 days of Asset_B:')
st.bar_chart(data.set_index('Time')['Asset_B'].tail(10))

# ---------------------------------------
# Section 3: Displaying Dynamic Graphs
# ---------------------------------------
st.header('3. Displaying Dynamic Graphs')

# Using Plotly
st.subheader('Plotly Interactive Chart')
st.write('An interactive Plotly chart of all assets:')

fig = px.line(data, x='Time', y=['Asset_A', 'Asset_B', 'Asset_C'], title='Assets Over Time')
st.plotly_chart(fig)

# ---------------------------------------
# Section 4: Adding Widgets for Interactivity
# ---------------------------------------
st.header('4. Adding Widgets for Interactivity')

# Slider Widget
st.subheader('Using a Slider')

# Allow the user to select a range of dates
st.write('Select a date range to view the data:')
start_date = st.date_input('Start date', data['Time'].min())
end_date = st.date_input('End date', data['Time'].max())

# Filter data based on the selected date range
filtered_data = data[(data['Time'] >= pd.to_datetime(start_date)) & (data['Time'] <= pd.to_datetime(end_date))]

st.write('Data from ', start_date, ' to ', end_date)
st.line_chart(filtered_data.set_index('Time'))

# Selectbox Widget
st.subheader('Using a Selectbox')

# Let the user choose which asset to display
asset = st.selectbox('Select an asset to display:', ['Asset_A', 'Asset_B', 'Asset_C'])
st.write(f'You selected: {asset}')

# Display the selected asset
st.line_chart(data.set_index('Time')[asset])

# Multiselect Widget
st.subheader('Using Multiselect')

# Allow the user to select multiple assets
assets_selected = st.multiselect('Select assets to compare:', ['Asset_A', 'Asset_B', 'Asset_C'], default=['Asset_A', 'Asset_B'])

# Display the selected assets
st.write('Comparing assets:', ', '.join(assets_selected))
st.line_chart(data.set_index('Time')[assets_selected])

# ---------------------------------------
# Section 5: Interactive Data Filtering
# ---------------------------------------
st.header('5. Interactive Data Filtering')

# Let the user filter data based on asset values
st.write('Filter data based on Asset_A value:')
asset_a_min = st.slider('Minimum Asset_A value', float(data['Asset_A'].min()), float(data['Asset_A'].max()), float(data['Asset_A'].min()))
asset_a_max = st.slider('Maximum Asset_A value', float(data['Asset_A'].min()), float(data['Asset_A'].max()), float(data['Asset_A'].max()))

# Filter the data
filtered_data = data[(data['Asset_A'] >= asset_a_min) & (data['Asset_A'] <= asset_a_max)]

st.write(f'Data where Asset_A is between {asset_a_min} and {asset_a_max}:')
st.dataframe(filtered_data)

# ---------------------------------------
# Section 6: Advanced Example - Financial Data Visualization
# ---------------------------------------
st.header('6. Advanced Example - Financial Data Visualization')

st.markdown("""
In this advanced example, we'll fetch real financial data and create an interactive
dashboard to visualize and analyze it.
""")

# Fetching real financial data using yfinance
st.subheader('Fetching Real Financial Data')

# Install yfinance if not already installed
# !pip install yfinance

import yfinance as yf

# Let the user input a ticker symbol
ticker_symbol = st.text_input('Enter a stock ticker symbol (e.g., AAPL, GOOG, MSFT):', 'AAPL')

# Fetch data for the selected ticker
@st.cache_data
def load_financial_data(ticker):
    """Fetches historical stock data for the given ticker symbol."""
    stock_data = yf.download(ticker, start='2020-01-01', end=pd.to_datetime('today'))
    return stock_data

if ticker_symbol:
    stock_data = load_financial_data(ticker_symbol.upper())

    st.write(f'Showing data for {ticker_symbol.upper()}:')
    st.dataframe(stock_data.tail())

    # Plot closing price
    st.subheader('Closing Price Over Time')
    st.line_chart(stock_data['Close'])

    # Plot volume
    st.subheader('Trading Volume Over Time')
    st.bar_chart(stock_data['Volume'])

    # Stock Price Analysis: Moving Averages
    st.subheader('Stock price Analysis')

    # Let the user select window sizes for moving averages
    short_window = st.number_input('Short-term moving average window:', min_value=1, max_value=50, value=20)
    long_window = st.number_input('Long-term moving average window:', min_value=1, max_value=200, value=100)

    # Calculate moving averages
    stock_data['Short_MA'] = stock_data['Close'].rolling(window=short_window).mean()
    stock_data['Long_MA'] = stock_data['Close'].rolling(window=long_window).mean()

    # Plot moving averages
    st.write('Closing Price with Moving Averages:')
    ma_fig = px.line(stock_data, x=stock_data.index, y=['Close', 'Short_MA', 'Long_MA'], labels={'value': 'Price', 'index': 'Date'})
    st.plotly_chart(ma_fig)


# ---------------------------------------
# Section 7: Conclusion
# ---------------------------------------
st.header('7. Conclusion')

st.markdown("""
In this tutorial, we've explored how Streamlit can be used to create interactive
web applications for data visualization. We've covered:

- Displaying static and interactive tables
- Creating various types of charts
- Adding widgets for user input
- Building an advanced financial data dashboard

**If you want to build streamlit application or modify the current example, you can use the following asset:**

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit API Reference](https://docs.streamlit.io/library/api-reference)
- [Plotly for Interactive Charts](https://plotly.com/python/)
- [yfinance for Financial Data](https://pypi.org/project/yfinance/)
""")

