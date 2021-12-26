import pyowm

owm = pyowm.OWM('e7452062026a13417d1b07460f684460', Language = "ru")
mgr = owm.weather_manager()

place = input('Где находишся ?Город/Страна')

observation = mgr.weather_at_place('London,GB')
w = observation.weather

print(w)