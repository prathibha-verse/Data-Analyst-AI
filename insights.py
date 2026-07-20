import pandas as pd


def generate_insights(filepath):

    if filepath.endswith(".csv"):

        df = pd.read_csv(filepath)

    elif filepath.endswith(".xlsx"):

        df = pd.read_excel(filepath)

    else:

        return ["Could not analyze the dataset."]

    insights = []

    text_columns = list(

        df.select_dtypes(include=["object"]).columns

    )

    numeric_columns = list(

        df.select_dtypes(include=["number"]).columns

    )

    # Dataset size

    if len(df) > 100000:

        insights.append(

            "This is a large dataset with more than 100,000 records."

        )

    # Missing values

    total_missing = int(

        df.isnull().sum().sum()

    )

    if total_missing > 0:

        insights.append(

            f"The dataset contains {total_missing} missing values."

        )

    # Negative values

    for column in numeric_columns:

        if df[column].min() < 0:

            insights.append(

                f"The '{column}' column contains negative values."

            )

    # Smart business insight

    if text_columns and numeric_columns:

        preferred_text_columns = [

            "Department",
            "Category",
            "Country",
            "City",
            "Branch"

        ]

        preferred_numeric_columns = [

            "Marks",
            "Sales",
            "Salary",
            "Attendance",
            "Quantity",
            "Amount"

        ]

        category_column = None
        value_column = None

        # Find best text column

        for col in preferred_text_columns:

            if col in df.columns:

                category_column = col
                break

        # Find best numeric column

        for col in preferred_numeric_columns:

            if col in df.columns:

                value_column = col
                break

        # Fallback

        if category_column is None:

            category_column = text_columns[0]

        if value_column is None:

            value_column = numeric_columns[0]

        grouped_data = (

            df.groupby(category_column)[value_column]

            .mean()

            .sort_values(ascending=False)

        )

        if not grouped_data.empty:

            top_category = grouped_data.index[0]

            top_value = grouped_data.iloc[0]

            insights.append(

                f"{top_category} has the highest average "

                f"{value_column} ({round(top_value, 2)})."

            )

    # Dataset structure

    insights.append(

        f"The dataset contains "

        f"{len(numeric_columns)} numeric columns and "

        f"{len(text_columns)} text columns."

    )

    return insights