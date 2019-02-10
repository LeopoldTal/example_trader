# -*- coding: utf-8 -*-
import requests

class Client:
	"""Price stream API client"""
	def __init__(self, url):
		self.url = url
		self.session = requests.Session() # to keep connection alive
	
	def get_price(self):
		"""C.get_price()
		
		Get the current asset price"""
		# TODO: maintain a session to keep the connection alive
		price_req = self.session.get(self.url)
		if price_req.status_code == 200:
			return int(price_req.text)
		else:
			raise requests.exceptions.RequestException(price_req.reason)
	
	def buy(self, buy_amount):
		"""C.buy(buy_amount)
		
		Buy (or sell if negative) the asset"""
		#print('%s %f' % (buy_amount < 0 and 'Selling' or 'Buying', buy_amount))
