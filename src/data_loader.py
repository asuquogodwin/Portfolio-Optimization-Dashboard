import yfinance as yf


def download_data(tickers, start_date, end_date):
    """
    Download adjusted closing prices from Yahoo Finance.
    """

    data = yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False,
    )

    return data["Close"]