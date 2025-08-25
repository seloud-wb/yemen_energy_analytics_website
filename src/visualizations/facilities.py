import pandas as pd
import plotly.express as px

def plot_facility_status_pie(df: pd.DataFrame, width: int = 600, height: int = 400):
    """
    Create a pie chart of facility status distribution.

    Parameters
    ----------
    df : pandas.DataFrame
        Facilities dataset with a 'Status' column.
    width : int
        Width of the chart in pixels.
    height : int
        Height of the chart in pixels.

    Returns
    -------
    fig : plotly.graph_objects.Figure
        Interactive pie chart figure.
    """
    # Count facilities by status
    status_counts = df['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']

    # Build pie chart
    fig = px.pie(
        status_counts,
        names="Status",
        values="Count",
        title="Facility Implementation Status",
        color="Status",
        hole=0.3,
        width=width,
        height=height
    )
    fig.update_traces(textinfo="percent+label")
    return fig
