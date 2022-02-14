from turtle import speed


def get_wind_class(speed):
	speed = int(input())
	if 1 <= get_wind_class <= 4:
		return "weak [1]"
	elif 5 <= get_wind_class <= 10:
		return "moderate [2]"
	elif 11 <= get_wind_class <= 18:
		return "strong [3]"
	elif 19 <= get_wind_class:
		return "hurricane [4]"

print(get_wind_class())
 