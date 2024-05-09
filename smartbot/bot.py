from smartbot.Translator import translate
from smartbot.weather import get_weather
from smartbot.calculator import calculate
from smartbot.Datetime import get_current_time
from smartbot.chatgpt import gpt_handle

callbacks = [
	(["время", "времени"], get_current_time, "None"),
	(["погода", "температура", "градусов"], get_weather, "query"),
	(["сколько будет", "вычисли", "чему равно"], calculate, "query"),
	(["переведи", "как переводится"], translate, "query"),
	([''], None, '')
]

def handle(query):
	for key_words, callback, status in callbacks:
		flag = False
		for word in key_words:
			if word in query:
				flag = True
				if status == "None":
					return callback()
				elif status == "query":
					return callback(query)
				elif status[:9] == "new query":
					new_query = input(status[9:] + ": ")
					return callback(new_query)
				else:
					return gpt_handle(query)
				
		if flag: break
	
	return ''


if __name__ == "__main__":
	print(handle(input('>')))
