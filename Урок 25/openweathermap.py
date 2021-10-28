from pyowm import OWM

owm = OWM('f7401a127f92925cd07a3379456ba257')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Москва,ru')
w = observation.weather


x = w.temperature('celsius')

print(observation.location.name, x["temp"])

