from geopy.geocoders import Nominatim
import time

locations = [
    "Airoli",
    "Aman Lodge",
    "Ambarnath",
    "Ambivli",
    "Andheri",
    "Asangaon",
    "Atgaon",
    "Badlapur",
    "Bandra",
    "Belapur CBD",
    "Bhandup",
    "Bhayandar",
    "Bhivpuri Road",
    "Bhiwandi Road",
    "Boisar",
    "Borivali",
    "Byculla",
    "Charni Road",
    "Chembur",
    "Chinchpokli",
    "Chunabhatti",
    "Churchgate",
    "Cotton Green",
    "CSMT",
    "Currey Road",
    "Dadar",
    "Diva",
    "Dombivli",
    "Ghansoli",
    "Goregaon",
    "Jogeshwari",
    "Kalva",
    "Kalyan",
    "Kandivali",
    "Kanjur Marg",
    "Karjat",
    "Kasara",
    "Khar Road",
    "Khopoli",
    "Kings Circle",
    "Kopar",
    "Kurla",
    "Lower Parel",
    "Mahim",
    "Malad",
    "Masjid",
    "Matheran",
    "Matunga",
    "Matunga Road",
    "Mira Road",
    "Mulund",
    "Mumbai Central",
    "Mumbra",
    "Nahur",
    "Naigaon",
    "Nalla Sopara",
    "Neral",
    "Nerul",
    "Palghar",
    "Panvel",
    "Parel",
    "Prabhadevi",
    "Santa Cruz",
    "Sion",
    "Thane",
    "Titwala",
    "Vashi",
    "Vasind",
    "Vikhroli",
    "Vile Parle",
    "Virar"
]

geolocator = Nominatim(user_agent="urbansense")

print("INSERT INTO Locations (area_name, city, latitude, longitude)")
print("VALUES")

rows = []

for place in locations:
    try:
        query = f"{place}, Maharashtra, India"
        location = geolocator.geocode(query)

        if location:
            city = "Navi Mumbai" if place in [
                "Airoli",
                "Ghansoli",
                "Nerul",
                "Vashi",
                "Belapur CBD"
            ] else "Mumbai"

            rows.append(
                f"('{place}', '{city}', "
                f"{location.latitude:.6f}, "
                f"{location.longitude:.6f})"
            )

            print(f"Found: {place}")

        else:
            print(f"Not found: {place}")

        time.sleep(1)

    except Exception as e:
        print(f"Error for {place}: {e}")

print(",\n".join(rows) + ";")