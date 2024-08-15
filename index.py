import plotly.express as px  # type: ignore
import polars as pl


def main():
    # Create a Polars DataFrame
    data = {
        'Region': ['Region 1', 'Region 2', 'Region 3', 'Region 4'] * 3,
        'Product': ['Product A'] * 4 + ['Product B'] * 4 + ['Product C'] * 4,
        'Sales': [150, 200, 300, 250, 100, 150, 250, 200, 80, 120, 180, 160],
    }

    df = pl.DataFrame(data)

    # Create a stacked bar chart using Plotly Express
    fig = px.bar(  # type: ignore
        df,
        x='Region',
        y='Sales',
        color='Product',
        title='Sales Distribution by Region',
        labels={'Sales': 'Sales', 'Region': 'Region'},
    )

    # Show the plot
    fig.show()  # type: ignore
