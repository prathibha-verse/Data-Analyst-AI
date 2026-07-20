import pandas as pd
import plotly.express as px


def generate_charts(filepath):

    # Read the file
    if filepath.endswith(".csv"):
        df = pd.read_csv(filepath)

    elif filepath.endswith(".xlsx"):
        df = pd.read_excel(filepath)

    else:
        return {
            "bar": "<p>Invalid file format.</p>",
            "pie": "<p>Invalid file format.</p>",
            "line": "<p>Invalid file format.</p>"
        }

    # Remove columns that contain only empty values
    df = df.dropna(axis=1, how="all")

    # Get text columns and numeric columns
    text_columns = list(
        df.select_dtypes(include=["object"]).columns
    )

    numeric_columns = list(
        df.select_dtypes(include=["number"]).columns
    )

    # Check whether we have enough columns
    if not text_columns or not numeric_columns:

        message = "<p>Not enough data to generate charts.</p>"

        return {
            "bar": message,
            "pie": message,
            "line": message
        }

    preferred_text_columns = [
        "Country",
        "Department",
        "Category",
        "City",
        "State",
        "Branch"
    ]

    preferred_numeric_columns = [
        "Sales",
        "Marks",
        "Quantity",
        "Amount",
        "Price",
        "Salary"
    ]

    x_column = None
    y_column = None

    for col in preferred_text_columns:

        if col in df.columns:

            x_column = col
            break

    for col in preferred_numeric_columns:

        if col in df.columns:

            y_column = col
            break

    if x_column is None:

        x_column = text_columns[0]

    if y_column is None:

        y_column = numeric_columns[0]

    grouped_data = (
        df.groupby(x_column)[y_column]
        .sum()
        .reset_index()
        .head(10)
    )

    if grouped_data.empty:

        message = "<p>No chart data available.</p>"

        return {
            "bar": message,
            "pie": message,
            "line": message
        }

    bar_chart = px.bar(
        grouped_data,
        x=x_column,
        y=y_column,
        title=f"{y_column} by {x_column}"
    )

    pie_chart = px.pie(
        grouped_data,
        names=x_column,
        values=y_column,
        title=f"{y_column} Distribution"
    )

    line_chart = px.line(
        grouped_data,
        x=x_column,
        y=y_column,
        title=f"{y_column} Trend"
    )

    return {
        "bar": bar_chart.to_html(full_html=False),
        "pie": pie_chart.to_html(full_html=False),
        "line": line_chart.to_html(full_html=False)
    }