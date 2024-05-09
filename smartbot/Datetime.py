from datetime import datetime 

def get_current_time():
	t = datetime.now()
	return "Текущее время: {}:{}:{}".format(
		t.hour,
		t.minute,
		t.second
	)
