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
		# collect some history before doing anything
		if len(price_history) < 10:
			return 0
		
		print('DEBUG: %.1f%% of my holdings should be in the asset'
			% (100 * self.kelly(price_history),))
		f_target = self.kelly(price_history)
		return (self.asset + self.cash/current_price) * f_target - self.asset
	
	def kelly(self, price_history):
		"""Get optimal fraction to invest in the asset according to the Kelly criterion"""
		gains = np.diff(price_history)
		wins = [ g for g in gains if g >= 0 ]
		losses = [ -g for g in gains if g < 0 ]
		if np.sum(wins) == 0:
			return 0
		if np.sum(losses) == 0:
			return 1
		p_win = len(wins) / len(gains)
		win_ratio = np.sum(wins) / np.sum(losses)
		return min(max(p_win - (1 - p_win)/win_ratio, 0), 1)
	
	def record_buy(self, buy_amount, price):
		"""A.record(buy_amount, price)
		
		Record a purchase or sale of the asset at the given unit price"""
		self.asset += buy_amount
		self.cash -= buy_amount * price
	
	def __str__(self):
		return 'Cash %.3f / Asset %.3f' % (self.cash, self.asset)
	
	def get_worth(self, current_price):
		"""A.get_worth(current_price)
		
		Gets total worth of agent's holdings given a price for the asset"""
		return self.cash + current_price * self.asset

