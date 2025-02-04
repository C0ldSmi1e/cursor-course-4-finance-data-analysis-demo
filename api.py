from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import uvicorn
import markdown2

from date_retriever import get_stock_data
from ai_analyzer import AIAnalyzer
from trader import get_trading_signal

app = FastAPI(
    title="Stock Analysis API",
    description="API for stock analysis using AI models",
    version="1.0.0"
)

# Templates configuration
templates = Jinja2Templates(directory="templates")

class StockAnalysisResponse(BaseModel):
    symbol: str
    date: str
    analysis: str
    trading_signal: str
    score: Optional[float]
    error: Optional[str] = None

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/", response_class=HTMLResponse)
async def analyze(
    request: Request,
    symbol: str = Form(...),
    date: str = Form(...)
):
    try:
        # Get stock data
        stock_data = get_stock_data(symbol, date)
        if stock_data is None:
            return templates.TemplateResponse(
                "index.html",
                {
                    "request": request,
                    "symbol": symbol,
                    "date": date,
                    "error": f"No data found for {symbol} on {date}"
                }
            )

        # Generate AI analysis
        analyzer = AIAnalyzer()
        analysis = analyzer.analyze_stock(symbol, stock_data)

        # Get trading signal
        signal_data = get_trading_signal(analysis)

        # Convert markdown to HTML
        analysis_html = markdown2.markdown(analysis)

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "symbol": symbol,
                "date": date,
                "analysis": analysis_html,
                "trading_signal": signal_data.get('signal', 'ERROR'),
                "score": signal_data.get('score'),
                "error": signal_data.get('error')
            }
        )

    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "symbol": symbol,
                "date": date,
                "error": str(e)
            }
        )

@app.get("/analyze/{symbol}", response_model=StockAnalysisResponse)
async def analyze_stock(symbol: str, date: str):
    """
    Analyze a stock for a given date
    
    Parameters:
    - symbol: Stock symbol (e.g., AAPL, MSFT)
    - date: Analysis date in YYYY-MM-DD format
    
    Returns:
    - Complete analysis with trading signals
    """
    try:
        # Validate date format
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Invalid date format. Please use YYYY-MM-DD"
            )

        # Get stock data
        stock_data = get_stock_data(symbol, date)
        if stock_data is None:
            raise HTTPException(
                status_code=404,
                detail=f"No data found for {symbol} on {date}"
            )

        # Generate AI analysis
        analyzer = AIAnalyzer()
        analysis = analyzer.analyze_stock(symbol, stock_data)

        # Get trading signal
        signal_data = get_trading_signal(analysis)

        # Prepare response
        return StockAnalysisResponse(
            symbol=symbol,
            date=date,
            analysis=analysis,
            trading_signal=signal_data.get('signal', 'ERROR'),
            score=signal_data.get('score'),
            error=signal_data.get('error')
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

if __name__ == "__main__":
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=3333,
        reload=True,
        log_level="info"
    ) 