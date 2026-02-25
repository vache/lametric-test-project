import io
import png
import base64

PIXEL = (0,128,0)
BLACK_PIXEL = (0, 0, 0)

class Icon:
	def __init__(self):
		# row = [*BLACK_PIXEL] * 8
		# self._rows = [row] * 8
		self._rows = [
			[*BLACK_PIXEL] * 8,
			[*BLACK_PIXEL] * 8,
			[*BLACK_PIXEL] * 8,
			[*BLACK_PIXEL] * 8,
			[*BLACK_PIXEL] * 8,
			[*BLACK_PIXEL] * 8,
			[*BLACK_PIXEL] * 8,
			[*BLACK_PIXEL] * 8
		]
		
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
			
	def write_file(self):
		writer = png.Writer(width=8, height=8, bitdepth=8, greyscale=False)
		with open("output.png", "wb") as f:
			writer.write(f, self._rows)
			
	def print_array(self):
		for row in self._rows:
			print(row)
		
if __name__ == "__main__":
	icon = Icon()
	for x in range(0, 8, 2):
		for y in range(0, 8, 2):
			r = x * 32
			g = y * 32
			b = y * 16 + x * 16
			print(x, y, r, g, b)
			icon.set_pixel(x, y, r, g, b)
			icon.set_pixel(x, y+1, r, g, b)
			icon.set_pixel(x+1, y, r, g, b)
			icon.set_pixel(x+1, y+1, r, g, b)
			icon.print_array()
	icon.write_file()
	
	print("icon:")
	print(icon.write())
	icon.print_array()
