import pandas as pd


def analyze_data(filepath):

    if filepath.endswith(".csv"):
        df = pd.read_csv(filepath)

    elif filepath.endswith(".xlsx"):
        df = pd.read_excel(filepath)

    else:
        return None

    numeric_df = df.select_dtypes(include=["number"])

    text_df = df.select_dtypes(include=["object"])

    summary = {

        "rows": df.shape[0],

        "columns": df.shape[1],

        "column_names": list(df.columns),

        "missing_values": df.isnull().sum().to_dict(),

        "total_missing_values": int(df.isnull().sum().sum()),

        "numeric_columns_count": len(numeric_df.columns),

        "text_columns_count": len(text_df.columns),

        "mean": numeric_df.mean().to_dict(),

        "median": numeric_df.median().to_dict(),

        "maximum": numeric_df.max().to_dict(),

        "minimum": numeric_df.min().to_dict()
    }

    return summary