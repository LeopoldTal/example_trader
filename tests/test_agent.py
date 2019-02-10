# -*- coding: utf-8 -*-
from .context import example_trader

def test_holds_if_knows_nothing():
	agent = example_trader.agent.Agent()
	buy_amount = agent.get_buy_amount(price_history=[], current_price=1.)
	assert(buy_amount) == 0

def test_no_buy_if_broke():
	agent = example_trader.agent.Agent()
	agent.cash = 0
	buy_amount = agent.get_buy_amount(price_history=[1000.,1000.,1000.1,999.9], current_price=1.)
	assert(buy_amount) == 0

def test_no_shorts():
	agent = example_trader.agent.Agent()
	agent.asset = 0
	buy_amount = agent.get_buy_amount(price_history=[.01,.01,0.011,0.009], current_price=1.)
	assert(buy_amount) == 0

def test_buys_at_huge_crash():
	agent = example_trader.agent.Agent()
	buy_amount = agent.get_buy_amount(price_history=[1000.,1000.,1000.1,999.9], current_price=1.)
	assert(buy_amount) > 0

def test_sells_at_huge_spike():
	agent = example_trader.agent.Agent()
	agent.asset = 42
	buy_amount = agent.get_buy_amount(price_history=[.01,.01,0.011,0.009], current_price=1.)
	assert(buy_amount) < 0

def test_records_buy():
	agent = example_trader.agent.Agent()
	agent.cash = 100
	agent.asset = 50
	agent.record_buy(buy_amount = 42, price = 0.1)
	assert(agent.asset == 92)
	assert(agent.cash == 95.8)
