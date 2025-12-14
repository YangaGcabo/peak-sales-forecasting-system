import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    df = df.sort_values("date")
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df = df.reset_index(drop=True)
    return df
