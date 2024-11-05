# Stock-Market-Prediction
This project is a stock prediction app built with Python and Streamlit. The app allows users to visualize historical stock data and forecast future trends using Facebook's Prophet model. Users can select different stocks and set a time frame for prediction, generating insightful data visualizations.

## Features
Stock Data Visualization: Displays the opening and closing prices of selected stocks over time.
Forecasting: Utilizes the Prophet model to predict future stock trends.
Interactive Interface: Users can select stocks and prediction periods easily.

## Requirements
Python 3.8+
Streamlit
Pandas
NumPy
Prophet
Plotly
yfinance

### To install the dependencies, use: pip install streamlit pandas numpy prophet plotly yfinance

## How to Run
1 Clone the repository.
2 Navigate to the project directory.
#### 3 Run the Streamlit app: streamlit run app.py
4 Open the provided local URL in your web browser.

## Code Explanation
Data Loading: Stock data is fetched using yfinance and displayed as raw data in a table.
Visualization: Plots the time series data for stock opening and closing prices.
Forecasting: The Prophet model is used for forecasting future trends.
Forecasts are visualized using Plotly charts, providing an intuitive look at the predicted trends.

## Usage
Select Stock: Choose a stock symbol from the dropdown list.
Set Prediction Period: Use the slider to set the number of years to predict (1-4 years).
View Forecasted Data: See raw forecast data along with interactive plots.

## File Structure
Predictionf6.py: The main application code.
README.md: Project description and instructions.

### Future Improvements
Adding more stock options and data sources.
Allowing for customized date ranges.
Improving prediction accuracy and adding other forecasting algorithms.
