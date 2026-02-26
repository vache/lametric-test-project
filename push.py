import time
from datetime import datetime
from random import randint
from requests import post

from frame import Frame
from icon import Icon
from stock import StockData

from env import BASIC_AUTH

ENDPOINT = "http://192.168.1.17:8080/api/v2/widget/update/com.lametric.diy.devwidget/9828dd4e73e84efba171e49b9f33e0b1"
RED_ICON = Icon(fill_color=(255,0,0))
GREEN_ICON = Icon(fill_color=(0,255,0))
BLUE_ICON = Icon(fill_color=(0,0,255))

def run():
	last_hour = None
	while(True):
		current_hour = datetime.now().hour
		if current_hour == last_hour:
			push_number()
		else:
			push_stock()
		last_hour = current_hour
		time.sleep(10)
	
def push_number():
	frame = Frame()
	num = randint(1,1000)
	if num % 3 == 0:
		frame.icon(RED_ICON.write())
	elif num % 3 == 1:
		frame.icon(GREEN_ICON.write())
	else:
		frame.icon(BLUE_ICON.write())
	frame.duration(10000)
	frame.text("教育漢字 " + str(num) + " 教育漢字")
	_push(frame)

def push_stock():
	data = StockData()
	frame = Frame()
	frame.duration(10000)
	value = float(data.fetch_latest_price("SHOP"))
	frame.text(f"SHOP: {value:.2f}")
	_push(frame)
	
def _push(frame):
	frames = {
		"frames": [frame.out()]
	}
	headers = {
		'Authorization': 'Basic ' + BASIC_AUTH
	}
	x = post(ENDPOINT, json=frames, headers=headers)	

if __name__ == "__main__":
	print("Pushing to endpoint: ", ENDPOINT)
	run()
