from flask import Flask
from frame import Frame
from icon import Icon

app = Flask(__name__)

def make_icon():
	icon = Icon()
	for x in range(0, 8, 2):
		for y in range(0, 8, 2):
			r = x * 32
			g = y * 32
			b = y * 16 + x * 16
			icon.set_pixel(x, y, r, g, b)
			icon.set_pixel(x, y+1, r, g, b)
			icon.set_pixel(x+1, y, r, g, b)
			icon.set_pixel(x+1, y+1, r, g, b)
	return icon.write()
				

@app.route("/")
def hello_world():
	hello = Frame()
	hello.text("hello")
	# hello.chartData(1, 2, 3, 4, 5)
	# hello.goalData(0, 3, 10)
	# return hello.out()
	hello.icon(make_icon())
	return {
		"frames": [hello.out()]
	}
	
