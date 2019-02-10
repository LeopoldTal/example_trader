# -*- coding: utf-8 -*-
from unittest import mock
from .context import example_trader

def get_loop():
	agent = mock.MagicMock()
	agent.get_buy_amount = mock.MagicMock(return_value = -3.14)
	
	client = mock.MagicMock()
	client.get_price = mock.MagicMock(return_value = 42)
	
	loop = example_trader.trading_loop.TradingLoop(agent, client)
	return loop

def test_steps():
	loop = get_loop()
	loop.step()
	
	loop.agent.get_buy_amount.assert_called_with([], 42)
	loop.client.buy.assert_called_with(-3.14)
	loop.agent.record_buy.assert_called_with(-3.14, 42)
