# -*- coding: utf-8 -*-
import numpy as np

class Agent:
	"""An agent, trading some asset against some currency"""
	def __init__(self):
		self.cash = 1000
		self.asset = 0
	
	"""A.get_buy_amount(price_history, current_price) -> float
	
	Get amount of the asset the agent wants to buy.
	Negative for selling, 0 for holding"""
	def get_buy_amount(self, price_history, current_price):
		print(price_history)
		if len(price_history) == 0:
			return 0
		
		# TODO: try diffs, there might be inertia in the market
		mean_price = np.mean(price_history)
		if current_price < mean_price: # TODO: what's a bid-ask spread, precious?
			if current_price <= self.cash:
				return 1 # TODO: pick some sensible amount; Kelly?
			else: # TODO: buy partial asset?
				return 0
		else:
			if self.asset >= 1:
				return -1
			else:
				return 0
	
	def record_buy(self, buy_amount, price):
		"""A.record(buy_amount, price)
		
		Record a purchase or sale of the asset at the given unit price"""
		self.asset += buy_amount
		self.cash -= buy_amount * price
	
	def __str__(self):
		return 'Cash %.3f / Asset %.3f' % (self.cash, self.asset)
