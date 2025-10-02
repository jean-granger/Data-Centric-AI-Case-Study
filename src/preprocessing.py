import pandas as pd
from sklearn.impute import SimpleImputer

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def summarize_missing(df: pd.DataFrame) -> pd.DataFrame:
    missing = df.isnull().sum()
    pct = (missing / len(df)) * 100
    return pd.DataFrame({'missing': missing, 'pct_missing': pct}).sort_values('pct_missing', ascending=False)

def basic_impute(df: pd.DataFrame, numeric_strategy='median'):
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    imputer = SimpleImputer(strategy=numeric_strategy)
    df[num_cols] = imputer.fit_transform(df[num_cols])
    return df

def save_processed(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)