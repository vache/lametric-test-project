from twelvedata import TDClient
from env import S_API_KEY

class StockData:
	def __init__(self):
		self._client = TDClient(apikey=S_API_KEY)

	def fetch_latest_price(self, symbol):
		return self._client.price(symbol=symbol).as_json()["price"]
	
	def fetch_day(self, symbol):
		return self._client.time_series(symbol=symbol, interval="1day", outputsize=1).as_json()
	
	def fetch_batch(self, symbol):
		return self._client.time_series(symbol=symbol, interval="1h", outputsize=8).as_json()

if __name__ == "__main__":
	data = StockData()
	print(data.fetch_latest_price("SHOP")["price"])
	# print(fetch_day("SHOP"))
	# batch = fetch_batch("SHOP")
	# for i in fetch_batch("SHOP"):
	#	print(i)
