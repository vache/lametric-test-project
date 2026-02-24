from flask import Flask
from frame import Frame
from icon import Icon

app = Flask(__name__)

@app.route("/")
def hello_world():
	# hello = Frame()
	# hello.text("hello")
	# hello.chartData(1, 2, 3, 4, 5)
	# hello.goalData(0, 3, 10)
	# return hello.out()
	icon = Icon()
	for x in range(1,6):
		for y in range(1,6):
			icon.set_pixel(x, y, 255, 255, 255)
	return icon.write()
