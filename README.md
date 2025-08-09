## Stock Price Analyzer (Tkinter + yfinance)

A simple desktop GUI application to visualize historical stock closing prices for a given ticker and date range. Built with Python, Tkinter, yfinance, and Matplotlib.

### Features
- **Ticker validation**: Checks if the provided ticker symbol is valid.
- **Date range input**: Fetches historical data between custom start/end dates (YYYY-MM-DD).
- **Interactive chart window**: Displays a Matplotlib line chart embedded in a Tkinter window.
- **Clear error messages**: Handles invalid tickers, empty datasets, and runtime errors gracefully.

---

## Prerequisites

- **Python**: 3.9+ recommended
- **Pip**: Latest version

Python packages:
- `yfinance`
- `matplotlib`
- `tkinter` (comes with standard Python on Windows/macOS; on some Linux distros install via OS package manager)

Linux users may need:
```bash
sudo apt-get update && sudo apt-get install -y python3-tk
```

---

## Installation

Using a virtual environment is recommended.

### Windows (PowerShell)
```powershell
py -m venv .venv
.venv\Scripts\Activate
pip install --upgrade pip
pip install yfinance matplotlib
```

### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install yfinance matplotlib
```

Alternatively, create a `requirements.txt`:
```txt
yfinance>=0.2.40
matplotlib>=3.7
```
Then install:
```bash
pip install -r requirements.txt
```

---

## Usage

1. Save the script (for example as `stock_analyzer.py`).
2. Run the application:
   - Windows:
     ```powershell
     python stock_analyzer.py
     ```
   - macOS/Linux:
     ```bash
     python3 stock_analyzer.py
     ```
3. In the GUI:
   - Enter a stock ticker (e.g., `AAPL`, `MSFT`, `TSLA`).
   - Enter start date and end date in `YYYY-MM-DD` format.
   - Click “Analiz Yap” to display the closing price chart in a new window.

---

## Example

- Ticker: `AAPL`
- Start: `2023-01-01`
- End: `2023-12-31`

A new window will open with a line chart for the closing prices across the selected date range.

---

## Project Structure

```text
.
├─ stock_analyzer.py        # Main Tkinter application using yfinance + Matplotlib
├─ requirements.txt         # Optional dependency pinning
└─ README.md
```

---

## Notes

- Date format must be `YYYY-MM-DD`.
- If the date range has no available data, the app will inform you.
- Network access is required for fetching data from Yahoo Finance via `yfinance`.
- Ticker validation uses `yfinance.Ticker(...).info`. If the upstream API changes or rate limits apply, validation behavior may vary.

---

## Troubleshooting

- “Invalid stock ticker”: Double-check the symbol (uppercase) and ensure it is listed on Yahoo Finance.
- “No data found for the specified dates”: Verify market trading days and date range.
- Tkinter errors on Linux: Install `python3-tk` via your package manager.
- SSL or network issues: Make sure your environment can reach Yahoo Finance and your system certificates are up to date.

---

## License

This project is provided under the MIT License. See `LICENSE` for details.

---

## Disclaimer

This software is for informational and educational purposes only and does not constitute financial advice. Always do your own research before making investment decisions.
