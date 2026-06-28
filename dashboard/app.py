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
st.title("Dashboard")
selected_area = st.selectbox(
    "Choose Area",
    ["All"] + list(area_df["area_name"])
)
st.metric("Total Environmental Records", len(df))
aqi_avg = round(df["aqi"].mean(), 2)
st.metric(
    "Average AQI",
    aqi_avg
)
st.metric("Max AQI", int(df["aqi"].max()))
st.metric("Min AQI", int(df["aqi"].min()))
st.metric("Average Temperature", round(df["temperature"].mean(), 2))
st.metric("Average Humidity", round(df["humidity"].mean(), 2))
st.dataframe(df.head(20))
area_df = pd.read_sql(area_query, conn)
fig2 = px.bar(
    area_df,
    x="area_name",
    y="avg_aqi",
    title="Average AQI by Area"
)
st.plotly_chart(fig2)
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
conn.close()