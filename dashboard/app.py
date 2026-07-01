import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
import os

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
query = """
SELECT *
FROM Env_Data
"""
df = pd.read_sql(query, conn)
area_query = """
SELECT
    l.area_name,
    ROUND(AVG(e.aqi),2) AS avg_aqi
FROM Env_Data e
JOIN Locations l
ON e.location_id = l.location_id
GROUP BY l.area_name
"""
area_df = pd.read_sql(area_query, conn)
st.title("UrbanSense")
st.caption("Smart Environmental Monitoring System Dashboard")
selected_area = st.selectbox(
    "Choose Area",
    ["All"] + list(area_df["area_name"])
)
location_query = """
SELECT
e.*, l.area_name
FROM Env_Data e
JOIN Locations l
ON e.location_id = l.location_id
"""
df = pd.read_sql(location_query, conn)
if selected_area != "All":
    df = df[df["area_name"] == selected_area]
if selected_area != "All":
    st.subheader("Location Details")
    col1, col2, col3 = st.columns(3)
    col1.metric(
        "AQI",
        round(df["aqi"].mean(), 2)
    )
    col2.metric(
        "PM2.5",
        round(df["pm25"].mean(), 2)
    )
    col3.metric(
        "PM10",
        round(df["pm10"].mean(), 2)
    )
    col1, col2 = st.columns(2)
    col1.metric(
        "Temperature",
        round(df["temperature"].mean(), 2)
    )
    col2.metric(
        "Humidity",
        round(df["humidity"].mean(), 2)
    )
col1, col2, col3, col4 = st.columns(4)
col1.metric("Records", len(df))
col2.metric("Avg AQI", round(df["aqi"].mean(), 2))
col3.metric("Max AQI", int(df["aqi"].max()))
col4.metric("Avg Temp", round(df["temperature"].mean(), 2))
st.dataframe(df)
worst_area = area_df.loc[area_df["avg_aqi"].idxmax()]
st.info(
    f" Highest average AQI detected in {worst_area['area_name']} "
    f"({worst_area['avg_aqi']})"
)
avg_aqi = round(df["aqi"].mean(), 2)
if avg_aqi <= 50:
    st.success("Air Quality: Good")
elif avg_aqi <= 100:
    st.warning("Air Quality: Moderate")
else:
    st.error("Air Quality: Poor")
fig2 = px.bar(
    area_df,
    x="area_name",
    y="avg_aqi",
    title="Average AQI by Area"
)
trend_query = """
SELECT
    DATE(recorded_at) AS day,
    ROUND(AVG(aqi),2) AS avg_aqi
FROM Env_Data
GROUP BY DATE(recorded_at)
ORDER BY day
"""
trend_df = pd.read_sql(trend_query, conn)
fig = px.line(
    trend_df,
    x="day",
    y="avg_aqi",
    title="AQI Trend Over Time"
)
ranking = area_df.sort_values(
    "avg_aqi",
    ascending=False
)
st.subheader("Most Polluted Areas")
st.dataframe(ranking)
st.plotly_chart(fig,use_container_width=True)
csv = df.to_csv(index=False)
st.plotly_chart(fig2,use_container_width=True)
map_query = """
SELECT
    l.area_name,
    l.latitude,
    l.longitude,
    ROUND(AVG(e.aqi),2) AS avg_aqi
FROM Env_Data e
JOIN Locations l
ON e.location_id = l.location_id
GROUP BY l.location_id
"""
map_df = pd.read_sql(map_query, conn)
st.subheader("Pollution Map")
st.map(
    map_df.rename(
        columns={
            "latitude": "lat",
            "longitude": "lon"
        }
    )
)
st.download_button(
    "Download Data",
    csv,
    "urbansense_data.csv",
    "text/csv"
)
conn.close()