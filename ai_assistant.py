import requests
import pandas as pd


def ask_ai(filepath, summary, question):

    if filepath.endswith(".csv"):

        df = pd.read_csv(filepath)

    else:

        df = pd.read_excel(filepath)

    sample_data = df.head(20).to_string()

    prompt = f"""
    You are an intelligent data analyst.

    Dataset summary:

    Rows: {summary["rows"]}

    Columns: {summary["columns"]}

    Column names:

    {summary["column_names"]}

    Mean values:

    {summary["mean"]}

    Maximum values:

    {summary["maximum"]}

    Minimum values:

    {summary["minimum"]}

    Here are the first 20 rows of the dataset:

    {sample_data}

    Answer the user's question clearly.

    Question:

    {question}
    """

    response = requests.post(

        "http://localhost:11434/api/generate",

        json={
            "model": "qwen2.5:3b",
            "prompt": prompt,
            "stream": False
        }

    )

    result = response.json()

    return result["response"]