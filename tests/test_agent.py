# -*- coding: utf-8 -*-
import pytest
from unittest import mock
from .context import example_trader

class TestKelly:
	def test_computes_kelly(self):
		agent = example_trader.agent.Agent()
		k = agent.kelly([10, 15, 5, 20])
		assert(k == pytest.approx(0.5))
	
	def test_clamps_if_infinite_win(self):
		agent = example_trader.agent.Agent()
		k = agent.kelly([1, 2, 3])
		assert(k == pytest.approx(1))
	
	def test_clamps_if_infinite_loss(self):
		agent = example_trader.agent.Agent()
		k = agent.kelly([3, 2, 1])
		assert(k == pytest.approx(0))

class TestStartup:
	def test_holds_if_knows_nothing(self):
		agent = example_trader.agent.Agent()
		buy_amount = agent.get_buy_amount(price_history=[], current_price=1.)
		assert(buy_amount == 0)
	
	def test_holds_on_startup(self):
		agent = example_trader.agent.Agent()
		buy_amount = agent.get_buy_amount(price_history=[1000.]*9, current_price=1.)
		assert(buy_amount == 0)

class TestClamping:
	def test_no_buy_if_broke(self):
		agent = example_trader.agent.Agent()
		agent.kelly = mock.MagicMock(return_value = 1)
		agent.cash = 0
		buy_amount = agent.get_buy_amount(price_history=[], current_price=1.)
		assert(buy_amount == 0)
	
	def test_no_shorts(self):
		agent = example_trader.agent.Agent()
		agent.kelly = mock.MagicMock(return_value = 0)
		agent.asset = 0
		buy_amount = agent.get_buy_amount(price_history=[], current_price=1.)
		assert(buy_amount == 0)

class TestKellyAgent:
	def test_holds_at_kelly(self):
		agent = example_trader.agent.Agent()
		agent.kelly = mock.MagicMock(return_value = 0.6)
		agent.cash = 40
		agent.asset = 6
		buy_amount = agent.get_buy_amount(price_history=[1]*1000, current_price=10)
		assert(buy_amount == 0)
	
	def test_buys_if_under_kelly(self):
		agent = example_trader.agent.Agent()
		agent.kelly = mock.MagicMock(return_value = 0.9)
		agent.cash = 40
		agent.asset = 6
		buy_amount = agent.get_buy_amount(price_history=[1]*1000, current_price=10)
		assert(buy_amount == 3)
	
	def test_sells_if_over_kelly(self):
		agent = example_trader.agent.Agent()
		agent.kelly = mock.MagicMock(return_value = 0.5)
		agent.cash = 40
		agent.asset = 6
		buy_amount = agent.get_buy_amount(price_history=[1]*1000, current_price=10)
		assert(buy_amount == -1)

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
