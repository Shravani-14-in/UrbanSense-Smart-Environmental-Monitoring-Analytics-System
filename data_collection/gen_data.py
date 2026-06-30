import mysql.connector
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os;
# Connect to MySQL
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = conn.cursor()
cursor.execute("""
SELECT location_id, area_name
FROM Locations
""")
locations = cursor.fetchall()
pollution_profile = {
    "Kurla": (120, 220),
    "Chembur": (110, 210),
    "Sion": (100, 190),
    "Dadar": (90, 180),
    "Andheri": (80, 170),
    "Bandra": (70, 150),
    "Powai": (60, 130),
    "Nerul": (50, 120),
    "Vashi": (50, 120),
    "Matheran": (20, 70)
}

records = []

for location_id, area_name in locations:

    aqi_low, aqi_high = pollution_profile.get(
        area_name,
        (60, 160)
    )

    for _ in range(100):

        aqi = random.randint(aqi_low, aqi_high)

        pm25 = round(aqi * random.uniform(0.35, 0.75), 2)
        pm10 = round(aqi * random.uniform(0.60, 1.20), 2)

        temperature = round(random.uniform(22, 38), 2)
        humidity = round(random.uniform(40, 95), 2)

        days_ago = random.randint(0, 30)
        hours_ago = random.randint(0, 23)

        recorded_at = (
            datetime.now()
            - timedelta(days=days_ago, hours=hours_ago)
        )

        records.append(
            (
                location_id,
                aqi,
                pm25,
                pm10,
                temperature,
                humidity,
                recorded_at
            )
        )

# Clear old data
cursor.execute("DELETE FROM Env_Data")

# Insert new data
cursor.executemany(
    """
    INSERT INTO Env_Data
    (
        location_id,
        aqi,
        pm25,
        pm10,
        temperature,
        humidity,
        recorded_at
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """,
    records
)
conn.commit()
print(f"Inserted {len(records)} records")
cursor.close()
conn.close()