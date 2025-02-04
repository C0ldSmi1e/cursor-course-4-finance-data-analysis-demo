import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_stock_comparison_plot(stock_data):
    """
    Create an interactive plot comparing stock prices with technical indicators
    
    Args:
        stock_data (dict): Dictionary containing DataFrames with historical data for each company
        
    Returns:
        plotly.graph_objects.Figure: Interactive plot figure
    """
    # Create figure with secondary y-axis
    fig = make_subplots(rows=3, cols=1, 
                        shared_xaxes=True,
                        vertical_spacing=0.05,
                        row_heights=[0.6, 0.2, 0.2],
                        subplot_titles=('Price and Moving Averages', 'RSI', 'MACD'))

    colors = {'Microsoft': '#00a8e8', 'Google': '#db4437', 
             'Amazon': '#ff9900', 'NVIDIA': '#76b900'}

    # Add price and indicators for each company
    for name, hist_data in stock_data.items():
        # Main price plot
        fig.add_trace(
            go.Scatter(x=hist_data.index, y=hist_data['Close'],
                      name=f"{name} Price",
                      line=dict(color=colors[name]),
                      hovertemplate='%{y:.2f}',
                      legendgroup=name),
            row=1, col=1
        )
        
        # Add moving averages for the first company only (to avoid cluttering)
        if name == 'Microsoft':
            fig.add_trace(
                go.Scatter(x=hist_data.index, y=hist_data['SMA_50'],
                          name='50-day MA',
                          line=dict(color='yellow', dash='dash'),
                          hovertemplate='%{y:.2f}'),
                row=1, col=1
            )
            fig.add_trace(
                go.Scatter(x=hist_data.index, y=hist_data['SMA_200'],
                          name='200-day MA',
                          line=dict(color='white', dash='dash'),
                          hovertemplate='%{y:.2f}'),
                row=1, col=1
            )
            
            # Add RSI
            fig.add_trace(
                go.Scatter(x=hist_data.index, y=hist_data['RSI'],
                          name='RSI',
                          line=dict(color='cyan'),
                          hovertemplate='%{y:.2f}'),
                row=2, col=1
            )
            
            # Add MACD
            fig.add_trace(
                go.Scatter(x=hist_data.index, y=hist_data['MACD'],
                          name='MACD',
                          line=dict(color='cyan'),
                          hovertemplate='%{y:.2f}'),
                row=3, col=1
            )
            fig.add_trace(
                go.Scatter(x=hist_data.index, y=hist_data['Signal_Line'],
                          name='Signal Line',
                          line=dict(color='yellow'),
                          hovertemplate='%{y:.2f}'),
                row=3, col=1
            )

    # Update layout
    fig.update_layout(
        title='Tech Giants Stock Analysis with Technical Indicators',
        template='plotly_dark',
        height=1200,  # Increased height for multiple subplots
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        xaxis=dict(rangeslider=dict(visible=False))  # Removed rangeslider for better visibility
    )

    # Add RSI lines
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
    fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)

    # Update y-axes labels
    fig.update_yaxes(title_text="Price (USD)", row=1, col=1)
    fig.update_yaxes(title_text="RSI", row=2, col=1)
    fig.update_yaxes(title_text="MACD", row=3, col=1)

    return fig

def show_plot(fig):
    """Display the plot"""
    fig.show() 