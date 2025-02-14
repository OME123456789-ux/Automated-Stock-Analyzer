import tkinter as tk
from tkinter import messagebox
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

# Create Figure and Axes objects globally
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

def retrieve_stock_data(company_name):
    """Fetch stock data using yfinance with error handling."""
    try:
        time.sleep(2)  # Avoid hitting rate limits
        stock_data = yf.download(company_name, start="2020-01-01", end="2023-07-01")

        # Debugging: Print retrieved data
        print(f"\nDownloaded Data for {company_name}:")
        print(stock_data.head())  
        print(f"\nAvailable columns: {list(stock_data.columns)}\n")

        if stock_data.empty:
            raise ValueError(f"No data found for {company_name}. Check the ticker symbol.")

        if "Adj Close" not in stock_data.columns and "Close" not in stock_data.columns:
            raise ValueError(f"Error: Neither 'Adj Close' nor 'Close' columns found. Available columns: {list(stock_data.columns)}")

        return stock_data
    except Exception as e:
        raise ValueError(f"Error retrieving stock data: {e}")

def calculate_portfolio_metrics(stock_data):
    """Calculate portfolio metrics while handling missing 'Adj Close'."""
    
    # Use "Close" if "Adj Close" is missing
    price_column = "Adj Close" if "Adj Close" in stock_data.columns else "Close"
    
    daily_returns = stock_data[price_column].pct_change().dropna()
    cumulative_returns = (daily_returns + 1).cumprod() - 1
    portfolio_value = stock_data[price_column].iloc[-1]

    portfolio_metrics = {
        "Portfolio Value": portfolio_value,
        "Daily Returns": daily_returns,
        "Cumulative Returns": cumulative_returns,
    }
    return portfolio_metrics

def create_portfolio_visualizations(stock_data):
    """Generate plots for stock price and daily returns."""
    try:
        price_column = "Adj Close" if "Adj Close" in stock_data.columns else "Close"
        daily_returns = stock_data[price_column].pct_change().dropna()

        axes[0].clear()
        axes[0].plot(daily_returns.index, daily_returns.values, label="Daily Returns", color='blue')
        axes[0].set_xlabel("Date")
        axes[0].set_ylabel("Daily Returns")
        axes[0].set_title("Daily Returns for Stock")
        axes[0].legend()

        axes[1].clear()
        axes[1].plot(stock_data.index, stock_data[price_column], label="Stock Price", color='green')
        axes[1].set_xlabel("Date")
        axes[1].set_ylabel("Stock Price")
        axes[1].set_title("Stock Price for Company")
        axes[1].legend()

        canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", f"Error creating visualizations: {e}")

def analyze_stock_portfolio():
    """Main function to retrieve stock data, analyze it, and display metrics."""
    company_name = company_entry.get().upper()  # Convert input to uppercase

    try:
        stock_data = retrieve_stock_data(company_name)
        portfolio_metrics = calculate_portfolio_metrics(stock_data)

        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, f"Calculated Portfolio Metrics for {company_name}:\n")
        
        for key, value in portfolio_metrics.items():
            if isinstance(value, pd.Series):  # Display first few values for series
                output_text.insert(tk.END, f"{key}:\n{value.head()}\n")
            else:
                output_text.insert(tk.END, f"{key}: {value}\n")

        create_portfolio_visualizations(stock_data)
    
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error occurred: {e}")

# GUI Setup
window = tk.Tk()
window.title("Automated Stock Portfolio Analyzer")

company_label = tk.Label(window, text="Enter Company Name:")
company_label.pack(pady=5)

company_entry = tk.Entry(window, width=30)
company_entry.pack(pady=5)

analyze_button = tk.Button(window, text="Analyze", command=analyze_stock_portfolio)
analyze_button.pack(pady=10)

output_text = tk.Text(window, height=15, width=50)
output_text.pack(pady=5)

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

window.mainloop()
