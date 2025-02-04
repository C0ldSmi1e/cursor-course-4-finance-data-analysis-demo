from date_retriever import get_stock_data
from ai_analyzer import AIAnalyzer
from trader import get_trading_signal

def main():
    try:
        # Initialize the AI analyzer
        analyzer = AIAnalyzer()
        
        # Get data for a specific stock
        symbol = 'AAPL'
        data = get_stock_data(symbol, '2024-03-20')
        
        # Generate AI analysis
        if data is not None:
            print("\nStock Data Summary:")
            print("=" * 80)
            print(f"Data shape: {data.shape}")
            print("\nLast 5 days of data:")
            print(data.tail())
            
            # Get the initial analysis
            print("\nGenerating AI Analysis...")
            analysis = analyzer.analyze_stock(symbol, data)
            print("\nAI Analysis:")
            print("=" * 80)
            print(analysis)
            
            # Get trading signal
            print("\nGenerating Trading Signal...")
            trading_signal = get_trading_signal(analysis)
            
            print(f"\nTrading Signal for {symbol}:")
            print("=" * 80)
            if 'error' in trading_signal:
                print(f"Error in trading signal: {trading_signal['error']}")
            print(f"Signal: {trading_signal['signal']}")
            print(f"Score: {trading_signal['score']}/10")
        else:
            print(f"Failed to retrieve data for {symbol}")
            
    except ValueError as e:
        print(f"Configuration Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()