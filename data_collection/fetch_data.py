import random
from datetime import datetime, timedelta
locations = [1, 2, 3, 4, 5, 6]
start_date = datetime(2025, 1, 1)
with open("sample_environmental_data.sql", "w") as f:
    f.write("INSERT INTO environmental_data ")
    f.write("(location_id, aqi, pm25, pm10, temperature, humidity, recorded_at)\nVALUES\n")
    rows = []
    for i in range(500):
        location_id = random.choice(locations)
        aqi = random.randint(40, 250)
        pm25 = round(random.uniform(10, 150), 2)
        pm10 = round(random.uniform(20, 200), 2)
        temperature = round(random.uniform(22, 38), 1)
        humidity = round(random.uniform(40, 90), 1)
        date = start_date + timedelta(hours=i)
        row = (
            f"({location_id}, {aqi}, {pm25}, "
            f"{pm10}, {temperature}, {humidity}, "
            f"'{date.strftime('%Y-%m-%d %H:%M:%S')}')"
        )
        rows.append(row)
    f.write(",\n".join(rows))
    f.write(";")
print("Generated 500 records!")