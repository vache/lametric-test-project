class Frame:
	def __init__(self):
		self._text = {}
		self._chartData = {}
		self._goalData = {}
		self._icon = {}
		self._duration = {}
		
	def out(self):
		return self._text | self._chartData | self._goalData | self._icon | self._duration

	def text(self, text):
		self._text = {
			"text": text
		}
		
	def goalData(self, start, current, end):
		self._goalData = {
			"goalData": {
				"start": start,
				"current": current,
				"end": end
			}
		}
		
	def chartData(self, *args):
		self._chartData = {
			"chartData": args
		}
	
	def icon(self, icon):
		self._icon = {
			"icon": icon
		}

	def duration(self, duration):
		self._duration = {
			"duration": duration
		}
