import os
from dotenv import load_dotenv
from together import Together
import json

class TradingSignalAnalyzer:
    def __init__(self):
        """Initialize the Trading Signal Analyzer with Together AI"""
        # Load environment variables
        load_dotenv()
        
        # Get API key from environment variables
        api_key = os.getenv('TOGETHER_API_KEY')
        if not api_key:
            raise ValueError("TOGETHER_API_KEY not found in environment variables")
            
        # Initialize Together client
        Together.api_key = api_key
        self.client = Together()
        self.model = "meta-llama/Llama-3.2-3B-Instruct-Turbo"

    def generate_trading_signal(self, analysis):
        """Generate trading signal based on the AI analysis"""
        if not analysis:
            return {
                'signal': 'ERROR',
                'score': None,
                'error': 'No analysis provided'
            }

        try:
            print("Sending request to Together AI...")
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": """You are a trading signal generator. You MUST return ONLY a valid JSON object with exactly this structure:
{"signal": <"Bullish" or "Bearish" or "Medium">, "score": <integer 1-10>}

Rules:
- signal must be exactly "Bullish", "Bearish", or "Medium"
- score must be an integer from 1 to 10 (1 = most bearish, 5 = neutral, 10 = most bullish)
- Return ONLY the JSON object, nothing else"""},
                    {"role": "user", "content": f"Based on this analysis, generate a trading signal:\n\n{analysis}"}
                ]
            )
            
            # Extract and parse response
            response_text = completion.choices[0].message.content.strip()
            print(f"\nRaw response from AI:\n{response_text}")
            
            try:
                result = json.loads(response_text)
                if 'signal' in result and 'score' in result:
                    if result['signal'] not in ["Bullish", "Bearish", "Medium"]:
                        raise ValueError("Invalid signal value")
                    if not isinstance(result['score'], (int, float)) or not 1 <= result['score'] <= 10:
                        raise ValueError("Invalid score value")
                    return {
                        'signal': result['signal'],
                        'score': float(result['score'])
                    }
                else:
                    raise ValueError("Response missing required fields")
                    
            except json.JSONDecodeError:
                raise ValueError("Failed to parse JSON response")
            
        except Exception as e:
            return {
                'signal': 'ERROR',
                'score': None,
                'error': f"Error in trading signal generation: {str(e)}"
            }

def get_trading_signal(analysis_text):
    """Helper function to get trading signal from analysis"""
    analyzer = TradingSignalAnalyzer()
    return analyzer.generate_trading_signal(analysis_text) 