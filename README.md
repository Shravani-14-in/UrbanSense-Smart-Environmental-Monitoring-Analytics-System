# UrbanSense-Smart-Environmental-Monitoring-Analytics-System
A real-time environmental intelligence platform that collects, stores, analyzes, and visualizes urban environmental data such as air quality, temperature, and humidity to generate actionable insights.

# 🌍 UrbanSense: Smart Environmental Monitoring & Analytics System

## 📌 Overview

UrbanSense is a smart environmental monitoring and analytics platform designed to collect, store, analyze, and visualize environmental data from urban locations.

The system focuses on environmental indicators such as Air Quality Index (AQI), temperature, humidity, and particulate matter levels to provide meaningful insights into urban environmental health.

---

## 🎯 Objectives

* Monitor environmental conditions across different locations.
* Store environmental data efficiently using MySQL.
* Perform analytics using advanced SQL queries.
* Rank locations based on environmental health.
* Visualize environmental trends through charts and maps.
* Support data-driven environmental awareness.

---

## 🚀 Features

### Current Features

* Environmental data storage
* AQI analysis
* Temperature monitoring
* Humidity tracking
* Environmental ranking system
* SQL-based analytics

### Planned Features

* Live AQI API integration
* Interactive map visualization
* Pollution heatmaps
* Environmental Health Score
* Automated data collection
* AQI forecasting

---

## 🛠️ Tech Stack

| Component            | Technology   |
| -------------------- | ------------ |
| Database             | MySQL        |
| Programming Language | Python       |
| Data Analysis        | Pandas       |
| Visualization        | Matplotlib   |
| Mapping              | Folium       |
| Version Control      | Git & GitHub |

---

## 🗄️ Database Schema

### Locations Table

| Column      | Type         |
| ----------- | ------------ |
| location_id | INT          |
| area_name   | VARCHAR(100) |
| city        | VARCHAR(100) |
| latitude    | DECIMAL(9,6) |
| longitude   | DECIMAL(9,6) |

### Environmental Data Table

| Column      | Type     |
| ----------- | -------- |
| record_id   | INT      |
| location_id | INT      |
| aqi         | INT      |
| pm25        | FLOAT    |
| pm10        | FLOAT    |
| temperature | FLOAT    |
| humidity    | FLOAT    |
| recorded_at | DATETIME |

---

## 📊 Analytics

UrbanSense provides insights such as:

* Most polluted locations
* Least polluted locations
* AQI trends over time
* Temperature analysis
* Humidity analysis
* Environmental health rankings
* High-risk environmental zones

---

## 📈 Sample Output

### Environmental Health Ranking

| Rank | Location    | AQI |
| ---- | ----------- | --- |
| 1    | Thane       | 45  |
| 2    | Navi Mumbai | 52  |
| 3    | Andheri     | 91  |
| 4    | Dadar       | 118 |
| 5    | Kurla       | 165 |

---

## 📂 Project Structure

```text
UrbanSense/
│
├── database/
│   ├── schema.sql
│   └── sample_data.sql
│
├── analytics/
│   ├── sql_queries.sql
│   └── reports/
│
├── visualization/
│   ├── charts/
│   └── maps/
│
├── data_collection/
│   └── fetch_data.py
│
├── README.md
│
└── requirements.txt
```

## 🌱 Vision

UrbanSense aims to transform environmental data into actionable insights, helping individuals and communities better understand and respond to environmental challenges.
