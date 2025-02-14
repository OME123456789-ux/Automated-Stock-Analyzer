# 📈 Automated Stock Analyzer

This project is a **Tkinter-based** automated stock analyzer that fetches stock data, calculates key portfolio metrics, and provides insightful visualizations.

## 🚀 Features

- Fetch real-time stock data using **Yahoo Finance (****`yfinance`****)**
- Calculate **daily returns**, **cumulative returns**, and **portfolio value**
- Generate **visualizations** for stock prices and returns
- User-friendly **Tkinter GUI** for seamless analysis
- Supports multiple **stock ticker symbols** (provided in `Tickers.xlsx`)

---

## 🛠 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Step 2: Install Dependencies

Ensure you have **Python 3.x** installed. Then, install the required libraries using:

```bash
pip install -r Requirements.txt
```

---

## ▶️ How to Run

### Step 1: Open a terminal in the project folder

### Step 2: Run the stock analyzer

```bash
python Stock_code.py
```

### Step 3: Enter a stock ticker

- The application will prompt you to enter a **company ticker**.
- Select any ticker from the provided **`Tickers.xlsx`** file.

### Step 4: Analyze Stock Data

- Click the **"Analyze"** button to fetch and visualize stock data.
- View **portfolio metrics** and graphical insights.

---

## 💂 Project Structure

```
📁 Automated-Stock-Analyzer
│── 📋 README.md         # Project documentation
│── 📋 Requirements.txt  # Python dependencies
│── 📋 Stock_code.py     # Main script for stock analysis (Tkinter GUI)
│── 📋 Tickers_sheet.py  # Generates `Tickers.xlsx` with stock symbols
│── 📋 Tickers.xlsx      # List of stock tickers (auto-generated)
```

---

## 📌 Dependencies

This project requires the following Python libraries:

```
matplotlib>=3.0.2
numpy>=1.15.2
pandas>=0.23.4
pandas-datareader>=0.7.0
seaborn>=0.11.0
statsmodels>=0.11.1
mplfinance>=0.12.7a4
yfinance>=0.2.4
openpyxl
```

These will be automatically installed using `pip install -r Requirements.txt`.

---
## Output Screenshots
![GOOGL_Stock_Image](https://github.com/user-attachments/assets/ba39b0b9-a309-4b95-b827-cedf79f25c04)

![UPS_Stock_Image](https://github.com/user-attachments/assets/6b4aa116-8b66-4a71-b057-4cf3d83ed558)


## 🤝 Contributing

Feel free to contribute by:

- Improving the **GUI**
- Adding **new stock analysis metrics**
- Optimizing **data retrieval methods**

Fork this repo and submit a **pull request**! 🚀

---

## 🐜 License

This project is licensed under the **MIT License**.

