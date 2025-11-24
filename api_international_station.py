import requests
import time

# Основной API для координат ISS
api_url_iss = 'http://api.open-notify.org/iss-now.json'

# Геолокационная служба OSM Nominatim
geocode_api_url = 'https://nominatim.openstreetmap.org/reverse'

# Делаем запрос на получение текущих координат ISS
response = requests.get(api_url_iss)

if response.status_code == 200:
    iss_data = response.json()
    latitude = float(iss_data['iss_position']['latitude'])
    longitude = float(iss_data['iss_position']['longitude'])

    # Готовим параметры для геолокационного запроса
    params = {
        'lat': latitude,
        'lon': longitude,
        'format': 'json',
        'zoom': 0  # Минимальный уровень детализации (страна)
    }

    # Заголовок агента пользователя
    headers = {'User-Agent': 'MyISSLocator/1.0'}

    # Запрашиваем страну по координатам
    geo_response = requests.get(geocode_api_url, params=params, headers=headers)

    if geo_response.status_code == 200:
        geo_data = geo_response.json()
        address = geo_data.get('address', {})
        country = address.get('country', '')
        region = address.get('region', '') or address.get('state', '')

        # Определяем местонахождение ISS
        location_description = ''
        if country:
            location_description = f'{country}'
        elif region:
            location_description = f'{region}'
        else:
            ocean_areas = {
                (-180, 0): 'Тихий океан',
                (0, 180): 'Атлантический океан',
                (0, -180): 'Индийский океан',
                (180, 0): 'Северный Ледовитый океан'
            }
            # Классифицируем точку нахождения по океану (пример грубой классификации)
            for area_range, ocean_name in ocean_areas.items():
                lon_min, lon_max = area_range
                if lon_min <= longitude <= lon_max:
                    location_description = f'над {ocean_name}'
                    break
            else:
                location_description = 'над водами океана'

        print(f"Текущие координаты ISS: широта={latitude}, долгота={longitude}")
        print(f"МКС сейчас пролета́ет {location_description}")
    else:
        print("Ошибка при получении страны:", geo_response.status_code)
else:
    print("Ошибка при получении координат ISS:", response.status_code)