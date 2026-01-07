import requests
import matplotlib.pyplot as plt

API_KEY = "ea31367812e76a5433dafd10d1efe539"
CITY = " New York"

url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

temps = []
times = []

for item in data["list"][:8]:
    temps.append(item["main"]["temp"])
    times.append(item["dt_txt"])

plt.figure(figsize=(10,5))
plt.plot(times, temps, marker='o')
plt.xticks(rotation=45)
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.title(f"Weather Forecast for {CITY}")
plt.tight_layout()
plt.show()
