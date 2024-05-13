import requests
import time
from smartbot.bot import handle as hd

token = [54, 53, 49, 48, 56, 55, 57, 51, 48, 53, 58, 65, 65, 69, 56, 51, 85, 85, 102, 116, 115, 50, 51, 109, 73, 106, 108, 112, 85, 53, 67, 68, 55, 81, 86, 55, 71, 84, 65, 109, 112, 113, 105, 122, 54, 89]
token = ''.join([chr(x) for x in token])

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = token


def sendMessage(chat_id, txt):
	requests.get('{url}{token}/sendMessage?chat_id={chat}&text={text}'.format(
		url=API_URL,
		token=BOT_TOKEN,
		chat=chat_id,
		text=txt
	))


def sendPhoto(chat_id, photo_url):
	requests.get('{url}{token}/sendPhoto?chat_id={chat}&photo={photo}'.format(
		url=API_URL,
		token=BOT_TOKEN,
		chat=chat_id,
		photo=photo_url
	))

offset = -2

for i in range(100):
	updates = requests.get('{url}{token}/getUpdates?offset={offset}'.format(
		url=API_URL,
		token=BOT_TOKEN,
		offset=offset + 1
	)).json()
	
	if updates['result']:
		chats = {}
		for result in updates['result']:
			offset = result['update_id']
			chat_id = result['message']['from']['id']
			query = result['message']['text']
			chats[chat_id] = (chats.get(chat_id, 0) + 1, query)
			
			
		for chat_id, (count, query) in chats.items():
			if count > 1:
				sendMessage(chat_id, 'Хватит так много отправлять сообщений! Я не успеваю их обрабатывать!')
			else:
				try:
					reply = hd(query)
					if reply is not None and reply != '':
						sendMessage(chat_id, reply)
				except:
					sendMessage(chat_id, 'Something went wrong...')

			
	time.sleep(1)

