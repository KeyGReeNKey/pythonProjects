import requests
import json
import os

api_key = "6599215f50704d65d19dc17ff4d6f289"
city_name = "Nevinnomyssk"  # Замените на имя нужного вам города


# Функция для получения данных о погоде с API OpenWeatherMap
def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data


# Получаем данные о погоде для указанного города
weather_data = get_weather_data(city_name)

# Извлекаем только данные о температуре в Цельсиях
temperature_celsius = weather_data["main"]["temp"] - 273.15

# Сохраняем температуру в отдельный файл
with open("температура сегодня.txt", "w") as file:
    file.write(str(round(temperature_celsius, 2), ))

# Открываем изображения в зависимости от температуры
if temperature_celsius < 10:
    os.system("start Cold.jpg")
elif temperature_celsius >= 10 and temperature_celsius < 20:
    os.system("start fine.jpg")
else:
    os.system("start hot.jpg")
