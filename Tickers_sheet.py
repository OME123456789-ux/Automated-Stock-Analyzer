import pandas as pd

stock_data = {
    'AAPL': 'Apple Inc.',
    'AMZN': 'Amazon.com Inc.',
    'GOOGL': 'Alphabet Inc. (Class A shares)',
    'MSFT': 'Microsoft Corporation',
    'FB': 'Meta Platforms, Inc.',
    'TSLA': 'Tesla, Inc.',
    'JPM': 'JPMorgan Chase & Co.',
    'BRK.B': 'Berkshire Hathaway Inc. (Class B shares)',
    'JNJ': 'Johnson & Johnson',
    'V': 'Visa Inc.',
    'WMT': 'Walmart Inc.',
    'NVDA': 'NVIDIA Corporation',
    'BABA': 'Alibaba Group Holding Limited',
    'PYPL': 'PayPal Holdings, Inc.',
    'DIS': 'The Walt Disney Company',
    'CRM': 'Salesforce.com Inc.',
    'NFLX': 'Netflix, Inc.',
    'VZ': 'Verizon Communications Inc.',
    'XOM': 'Exxon Mobil Corporation',
    'BA': 'The Boeing Company',
    'ADBE': 'Adobe Inc.',
    'PFE': 'Pfizer Inc.',
    'KO': 'The Coca-Cola Company',
    'GOOG': 'Alphabet Inc. (Class C shares)',
    'INTC': 'Intel Corporation',
    'IBM': 'International Business Machines Corporation',
    'AMD': 'Advanced Micro Devices, Inc.',
    'UPS': 'United Parcel Service, Inc.',
    'NKE': 'Nike, Inc.',
    'GS': 'The Goldman Sachs Group, Inc.',
    'MS': 'Morgan Stanley',
    'CVS': 'CVS Health Corporation',
    'ABNB': 'Airbnb, Inc.',
    'SNAP': 'Snap Inc.',
    'SQ': 'Square, Inc.',
    'UBER': 'Uber Technologies, Inc.',
    'NOW': 'ServiceNow, Inc.',
    'ZM': 'Zoom Video Communications, Inc.',
    'ROKU': 'Roku, Inc.',
    'CRWD': 'CrowdStrike Holdings, Inc.',
    'NET': 'Cloudflare, Inc.',
    'MCD': 'McDonald\'s Corporation',
    'PEP': 'PepsiCo, Inc.',
    'NOK': 'Nokia Corporation',
    'WFC': 'Wells Fargo & Co.',
    'LMT': 'Lockheed Martin Corporation'
}

df = pd.DataFrame(list(stock_data.items()), columns=['Symbol', 'Company'])

# Handle duplicate ticker symbols
df = df.drop_duplicates(subset='Symbol', keep='first')

# Save to an Excel file
file_path = 'Tickers.xlsx'
df.to_excel(file_path, index=False, engine='openpyxl')

print(f'Stock data has been saved to {file_path}.')
