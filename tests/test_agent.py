# -*- coding: utf-8 -*-
from .context import example_trader

class TestStartup:
	def test_holds_if_knows_nothing(self):
		agent = example_trader.agent.Agent()
		buy_amount = agent.get_buy_amount(price_history=[], current_price=1.)
		assert(buy_amount) == 0

class TestClamping:
	def test_no_buy_if_broke(self):
		agent = example_trader.agent.Agent()
		agent.cash = 0
		buy_amount = agent.get_buy_amount(price_history=[1000.,1000.,1000.1,999.9], current_price=1.)
		assert(buy_amount) == 0
	
	def test_no_shorts(self):
		agent = example_trader.agent.Agent()
		agent.asset = 0
		buy_amount = agent.get_buy_amount(price_history=[.01,.01,0.011,0.009], current_price=1.)
		assert(buy_amount) == 0

class TestSanity:
	def test_buys_at_huge_crash(self):
		agent = example_trader.agent.Agent()
		buy_amount = agent.get_buy_amount(price_history=[1000.,1000.,1000.1,999.9], current_price=1.)
		assert(buy_amount) > 0

	def test_sells_at_huge_spike(self):
		agent = example_trader.agent.Agent()
		agent.asset = 42
		buy_amount = agent.get_buy_amount(price_history=[.01,.01,0.011,0.009], current_price=1.)
		assert(buy_amount) < 0

class TestRecord:
	def test_records_buy(self):
		agent = example_trader.agent.Agent()
		agent.cash = 100
		agent.asset = 50
		agent.record_buy(buy_amount = 42, price = 0.1)
		assert(agent.asset == 92)
		assert(agent.cash == 95.8)

class TestDiagnostics:
	def test_str(self):
		agent = example_trader.agent.Agent()
		agent.cash = 2.71
		agent.asset = 42
		assert(str(agent) == 'Cash 2.710 / Asset 42.000')

	def test_gets_worth(self):
		agent = example_trader.agent.Agent()
		agent.cash = 5
		agent.asset = 10
		assert(agent.get_worth(20) == 205)
