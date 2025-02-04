# 1

I am using @yfinance , please give me MSFT's data (past 100 days)

# 2

Please use @Plotly to visualize the data.

# 3

Please give me more tickers, like google, amazon, nvidia

# 4

Please put all the tickers in one chart.

# 5

Please use the past 10 years' data.

# 6

Please review the code, and split it into "date_retriever.py" and "date_visualizer.py"

# 7

Please tell me some common technical indicators in stock trading.

# 8

Now, please update the @date_retriever.py . It should take two parameters: symbol and date, then it will return the past 200 days' data from the date.

# 9

I will use @Together AI with "meta-llama/Llama-3.3-70B-Instruct-Turbo" model, which will take the raw data, and give a prediction based on the histrorical data. Please write a "ai_analyzer.py"

# 10

Please tell me how to install together AI's SDK, also, I will use python-dotenv to manage environment variables.

# 11

Please build a "trader.py", which takes the result of @ai_analyzer.py , pass it to @Together AI with "deepseek-ai/DeepSeek-R1" model. Review the analysis, give a signal of "Bullish, Bearish, or Medium", or you can give a score (10), where 1 represents bearish, 5 represents medium and 10 represents bullish. Remember you should only return the signal and score.

# 12

Please update the prompt again, it should NOT return any other content apart from the json.

# 13

Please use @UVicorn and @FastAPI to build an API, where there's an endpoint. This endpoint will take two parameters, symbol and date, and return the analysis, signal, and score.

# 14

Please tell me how to install neccessary packages.

# 15

please use port 3333

# 16

This is the output from api:
```
{
"symbol": "AAPL",
"date": "2024-03-20",
"analysis": "**Comprehensive Analysis of the Current Market Position:**\n\nApple Inc. (AAPL) is currently trading at $175.45, with a weekly gain of 2.89% and a monthly loss of 3.42%. The stock's price action suggests a short-term rebound, but the overall trend remains bearish, as evidenced by the stock trading below its 200-day moving average ($182.74). The relative strength index (RSI) of 39.08 indicates neutral conditions, neither overbought nor oversold. The moving average convergence divergence (MACD) is above the signal line, which is a bullish sign, but the MACD value is negative (-3.05), indicating that the stock's momentum is still bearish.\n\n**Key Technical Signals and Their Implications:**\n\n1. **RSI (39.08)**: The neutral RSI reading suggests that the stock is not experiencing extreme buying or selling pressure. This could lead to a period of consolidation or a potential reversal.\n2. **MACD (-3.05)**: The MACD is above the signal line, which is a bullish sign. However, the negative MACD value indicates that the stock's momentum is still bearish. A crossover above the signal line could lead to a bullish reversal.\n3. **50-day and 200-day MA**: The stock is trading below both its 50-day ($182.25) and 200-day ($182.74) moving averages, indicating a bearish trend. A break above these levels could lead to a reversal.\n4. **Volume (55,215,200)**: The high volume suggests that there is significant interest in the stock, which could lead to increased volatility.\n\n**Potential Support and Resistance Levels:**\n\n1. **Support**: $172.41 (recent low), $165.00 (psychological support), and $160.00 (long-term support)\n2. **Resistance**: $182.25 (50-day MA), $182.74 (200-day MA), and $190.00 (psychological resistance)\n\n**Short-term (1-2 weeks) Outlook:**\n\nThe short-term outlook for AAPL is neutral to slightly bullish. The stock's recent rebound and the MACD's position above the signal line suggest that the stock could continue to rise in the short term. However, the bearish trend and the stock's position below its moving averages suggest that the upside is limited. A break above the 50-day MA ($182.25) could lead to a short-term rally, while a break below the recent low ($172.41) could lead to a continuation of the bearish trend.\n\n**Medium-term (1-3 months) Outlook:**\n\nThe medium-term outlook for AAPL is bearish. The stock's position below its 200-day MA and the negative MACD value suggest that the stock's momentum is still bearish. A break below the long-term support level ($160.00) could lead to a significant decline, while a break above the 200-day MA ($182.74) could lead to a reversal. The stock's ability to hold above the 50-day MA ($182.25) will be crucial in determining the medium-term trend.\n\n**Key Risks and Factors to Watch:**\n\n1. **Earnings Report**: The upcoming earnings report will be a significant catalyst for the stock. A positive earnings surprise could lead to a rally, while a negative surprise could lead to a decline.\n2. **Market Sentiment**: The overall market sentiment will play a significant role in determining the stock's trend. A decline in market sentiment could lead to a decline in AAPL, while an improvement in sentiment could lead to a rally.\n3. **Competition**: The increasing competition in the tech industry, particularly from companies like Samsung and Huawei, could lead to a decline in AAPL's market share and revenue.\n4. **Regulatory Risks**: The ongoing regulatory scrutiny, particularly with regards to antitrust laws, could lead to a decline in AAPL's stock price.\n\nIn conclusion, AAPL's current market position is neutral to slightly bullish in the short term, but bearish in the medium term. The stock's ability to break above its moving averages and hold above its support levels will be crucial in determining the trend. Investors should closely monitor the earnings report, market sentiment, competition, and regulatory risks to make informed investment decisions.",
"trading_signal": "Medium",
"score": 5,
"error": null
}
```

Please build a web page, where users can input symbol and date. After processing, the page will display the signal and score, as well as the analysis in markdown format.