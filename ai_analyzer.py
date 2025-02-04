import os
from dotenv import load_dotenv
from together import Together
import pandas as pd
import numpy as np

class AIAnalyzer:
    def __init__(self):
        """Initialize the AI Analyzer with Together AI client"""
        # Load environment variables
        load_dotenv()
        
        # Get API key from environment variables
        api_key = os.getenv('TOGETHER_API_KEY')
        if not api_key:
            raise ValueError("TOGETHER_API_KEY not found in environment variables")
            
        # Initialize Together client
        Together.api_key = api_key
        self.client = Together()

        self.model = "meta-llama/Llama-3.3-70B-Instruct-Turbo"

    def prepare_data_summary(self, df):
        """
        Prepare a summary of the stock data for the AI model
        
        Args:
            df (pandas.DataFrame): Historical stock data with technical indicators
        
        Returns:
            str: Formatted summary of the stock data
        """
        # Get the most recent data
        latest_data = df.iloc[-1]
        week_ago = df.iloc[-5]  # Assuming 5 trading days in a week
        month_ago = df.iloc[-22]  # Assuming 22 trading days in a month
        
        # Calculate key metrics
        price_change_week = ((latest_data['Close'] - week_ago['Close']) / week_ago['Close']) * 100
        price_change_month = ((latest_data['Close'] - month_ago['Close']) / month_ago['Close']) * 100
        
        # Prepare the summary
        summary = f"""
Stock Analysis Summary:
1. Current Price: ${latest_data['Close']:.2f}
2. Price Changes:
   - Weekly: {price_change_week:.2f}%
   - Monthly: {price_change_month:.2f}%
3. Technical Indicators:
   - RSI: {latest_data['RSI']:.2f}
   - MACD: {latest_data['MACD']:.2f}
   - Signal Line: {latest_data['Signal_Line']:.2f}
   - 50-day MA: ${latest_data['SMA_50']:.2f}
   - 200-day MA: ${latest_data['SMA_200']:.2f}
4. Volume: {latest_data['Volume']:,.0f}
5. Price Range:
   - High: ${latest_data['High']:.2f}
   - Low: ${latest_data['Low']:.2f}

Recent Trends:
- The stock is trading {'above' if latest_data['Close'] > latest_data['SMA_200'] else 'below'} its 200-day moving average
- RSI indicates {'overbought' if latest_data['RSI'] > 70 else 'oversold' if latest_data['RSI'] < 30 else 'neutral'} conditions
- MACD is {'above' if latest_data['MACD'] > latest_data['Signal_Line'] else 'below'} the signal line
"""
        return summary

    def generate_analysis(self, df, symbol):
        """Generate AI analysis and predictions for the stock"""
        # Prepare the data summary
        data_summary = self.prepare_data_summary(df)
        
        try:
            # Generate the analysis using Together AI
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[{
                    "role": "user",
                    "content": f"""You are an expert financial analyst. Based on the following technical analysis data for {symbol}, please provide:
1. A comprehensive analysis of the current market position
2. Key technical signals and their implications
3. Potential support and resistance levels
4. Short-term (1-2 weeks) and medium-term (1-3 months) outlook
5. Key risks and factors to watch

Technical Data:
{data_summary}

Please provide a detailed, professional analysis with specific insights and actionable information."""
                }]
            )
            
            return completion.choices[0].message.content
            
        except Exception as e:
            return f"Error generating AI analysis: {str(e)}"

    def analyze_stock(self, symbol, data):
        """
        Main method to analyze a stock
        
        Args:
            symbol (str): Stock symbol
            data (pandas.DataFrame): Historical stock data
            
        Returns:
            str: Complete analysis report
        """
        if data is None or data.empty:
            return f"Error: No data available for {symbol}"
          

        analysis = self.generate_analysis(data, symbol)
        return analysis 