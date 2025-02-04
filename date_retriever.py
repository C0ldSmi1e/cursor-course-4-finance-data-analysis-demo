import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def calculate_technical_indicators(df):
    """Calculate technical indicators for a given stock DataFrame"""
    # Calculate moving averages
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()
    
    # Calculate RSI
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # Calculate MACD
    exp1 = df['Close'].ewm(span=12, adjust=False).mean()
    exp2 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = exp1 - exp2
    df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()
    
    return df

def get_stock_data(symbol, end_date):
    """
    Retrieve historical stock data for a specific symbol and date range
    
    Args:
        symbol (str): Stock symbol (e.g., 'MSFT', 'GOOGL')
        end_date (str): End date in 'YYYY-MM-DD' format
        
    Returns:
        pandas.DataFrame: DataFrame containing historical data with technical indicators
    """
    try:
        # Convert end_date string to datetime
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        
        # Calculate start date (200 trading days before end_date)
        # Adding extra days to account for weekends and holidays
        start_date = end_date - timedelta(days=300)
        
        # Get stock data
        stock = yf.Ticker(symbol)
        hist_data = stock.history(start=start_date.strftime('%Y-%m-%d'),
                                end=end_date.strftime('%Y-%m-%d'))
        
        # Ensure we have exactly 200 days of data
        if len(hist_data) > 200:
            hist_data = hist_data.tail(200)
        
        # Add technical indicators
        hist_data = calculate_technical_indicators(hist_data)
        
        return hist_data
        
    except Exception as e:
        print(f"Error retrieving data for {symbol}: {str(e)}")
        return None

def get_tech_stocks_data(end_date):
    """
    Retrieve historical stock data for major tech companies
    
    Args:
        end_date (str): End date in 'YYYY-MM-DD' format
        
    Returns:
        dict: Dictionary containing DataFrames with historical data for each company
    """
    # Define tickers
    tickers = {
        'MSFT': 'Microsoft',
        'GOOGL': 'Google',
        'AMZN': 'Amazon',
        'NVDA': 'NVIDIA'
    }
    
    # Retrieve data for each ticker
    stock_data = {}
    for ticker, name in tickers.items():
        hist_data = get_stock_data(ticker, end_date)
        if hist_data is not None:
            stock_data[name] = hist_data
    
    return stock_data 