### **Cryptocurrency Price Tracker**

## Overview

For the next 15 days, I'll be creating and sharing 15 projects – one per day! Free versions will be open to all on my GitHub, and a low-cost paid version will be available too. Can't wait to hear your thoughts!

The **Cryptocurrency Price Tracker** is a Python-based application that allows users to fetch real-time cryptocurrency prices and market data using the **CoinGecko API**. This tool is ideal for crypto enthusiasts and investors who need quick access to live price data for various cryptocurrencies.

This includes:
- Real-time cryptocurrency prices in USD.
- Market data such as market cap and 24-hour trading volume.
- A simple and user-friendly **Tkinter GUI**.
- Option to export data to a CSV file.

---

## Features

- Fetch live prices for any cryptocurrency.
- View additional market data, including market cap and 24-hour trading volume.
- Track multiple cryptocurrencies in one session.
- Export the fetched data to a CSV file for further analysis.

## Want more features? Upgrade to the Advanced Cryptocurrency Price Tracker with Enhanced Features for just **INR 299** at https://topmate.io/kartikeyahere/1342937

**Advanced Features:**
**Real-Time Price Data:**

- Fetch live prices, market cap, and 24-hour trading volume.
**Historical Data:**

- View price trends over a customizable period (1-365 days).
- Line charts for historical trends.

**Multi-Currency Support:**

- Display prices in USD, EUR, or GBP.

**Export Functionality:**

- Save both live and historical data to CSV files for offline analysis.

**Interactive Dashboard:**

- Built with Streamlit for a user-friendly and visually appealing interface.
  
**Special Offer:**

##Use the code **"cryptoapp"** at checkout to get **25% off instantly.**



---

## Folder Structure

Below is the folder structure of the project:

```bash
CryptoPriceTracker/
├── data/                         
│   ├── sample_data/              # Folder for storing sample price data
├── gui/                          
│   ├── __init__.py               # Initializes the GUI module
│   ├── crypto_gui.py             # GUI implementation for the application
├── utils/                        
│   ├── __init__.py               # Initializes the utils module
│   ├── crypto_api.py             # Logic to fetch cryptocurrency data from CoinGecko API
│   ├── export_csv.py             # Logic to export fetched data to CSV
├── main.py                       # Main entry point for the application
├── requirements.txt              # List of dependencies for the project
├── README.md                     # Documentation for the project
```

---

## Installation and Setup

### Prerequisites

Make sure you have the following installed on your system:

- **Python 3.8+**
- **pip**: Python's package manager.

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/thekartikeyamishra/CryptoPriceTracker.git
   cd CryptoPriceTracker
   ```

2. **Set Up Virtual Environment**

   Create and activate a virtual environment to isolate dependencies:
   - On **Windows**:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```

3. **Install Dependencies**

   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   Start the application by running the `main.py` script:
   ```bash
   python main.py
   ```

---

## How to Use

1. Launch the application by running `main.py`.
2. Enter the name of the cryptocurrency you want to track (e.g., `bitcoin` or `ethereum`).
3. Click **"Fetch Price"** to get the live price and market data.
4. View the details in the text box:
   - Cryptocurrency name
   - Price in USD
   - Market cap in USD
   - 24-hour trading volume in USD
5. To save the data, click **"Export to CSV"**. The data will be saved to a file named `crypto_data.csv`.

---

## Example Output

**In the GUI**:
```
Cryptocurrency: Bitcoin
Price (USD): 65000
Market Cap (USD): 1.2T
24h Volume (USD): 30B
```

**Exported CSV**:
```csv
Cryptocurrency,Price (USD),Market Cap (USD),24h Volume (USD)
Bitcoin,65000,1.2T,30B
```

---

## Dependencies

The project uses the following Python libraries:
- `requests`: For making API calls to fetch cryptocurrency data.
- `tkinter`: For building the graphical user interface.
- `csv`: For exporting data to a CSV file.

To install all dependencies, run:
```bash
pip install -r requirements.txt
```


## Acknowledgments

- **CoinGecko API**: Used for fetching live cryptocurrency data.
- **Python**: The programming language used to build this application.
- **Tkinter**: For the graphical user interface.

---
