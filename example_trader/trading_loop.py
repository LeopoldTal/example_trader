# -*- coding: utf-8 -*-
from time import sleep

class TradingLoop:
	"""Main trading agent loop
	
	Check price, decide whether to buy/sell, sleep, repeat"""
	def __init__(self, agent, client):
		self.agent = agent
		self.client = client
		self.price_history = []
	
	def step(self):
		current_price = self.client.get_price()
		buy_amount = self.agent.get_buy_amount(self.price_history[:], current_price)
		
		self.client.buy(buy_amount)
		# TODO: handle buy order failure, if that was possible
		self.agent.record_buy(buy_amount, current_price)
		
		self.price_history.append(current_price)
	
	def run(self):
		while True:
			self.step()
			sleep(2) # TODO: how hard can we pound on the API?
