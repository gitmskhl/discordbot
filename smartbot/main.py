from Translator import translate
from weather import get_weather
from calculator import calculate
from Datetime import get_current_time


callbacks = [
	(["время", "времени"], get_current_time, "None"),
	(["погода", "температура", "градусов"], get_weather, "query"),
	(["сколько будет", "вычисли", "чему равно"], calculate, "query"),
	(["переведи", "как переводится"], translate, "new query Enter the text")
]

while True:
	query = input("> ").lower()
	for key_words, callback, status in callbacks:
		flag = False
		for word in key_words:
			if word in query:
				flag = True
				if status == "None":
					callback()
				elif status == "query":
					callback(query)
				elif status[:9] == "new query":
					new_query = input(status[9:] + ": ")
					callback(new_query)
				
		if flag: break


