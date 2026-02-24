import io
import png
import base64

PIXEL = (0,128,0)
BLACK_PIXEL = (0, 0, 0)

class Icon:
	def __init__(self):
		row = [*BLACK_PIXEL] * 8
		self._rows = [row] * 8
		
	def set_pixel(self, x, y, r, g, b):
		# r, g, b = *pixel
		row = self._rows[y]
		index = 3 * x
		row[index] = r
		row[index + 1] = g
		row[index + 2] = b

	def write(self):
		writer = png.Writer(width=8, height=8, bitdepth=8, greyscale=False)
		with io.BytesIO() as b:
			writer.write(b, self._rows)
			encoded = base64.b64encode(b.getvalue())
			return "data:image/png;base64," + encoded.decode('utf-8')
		
if __name__ == "__main__":
	icon = Icon()
	for x in range(1,6):
		for y in range(1,6):
			icon.set_pixel(x, y, 255, 255, 255)
	
	print("icon:")
	print(icon.write())
		
