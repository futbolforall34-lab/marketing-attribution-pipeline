import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Conversion'] = df['Conversion'].map({'Yes': 1, 'No': 0})
    return df.sort_values(['User ID', 'Timestamp'])
