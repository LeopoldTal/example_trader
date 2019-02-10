# -*- coding: utf-8 -*-
from . import client
from . import agent
from . import trading_loop

API_URL = 'https://price-stream-api.herokuapp.com/'

if __name__ == '__main__':
	agent = agent.Agent()
	client = client.Client(API_URL)
	loop = trading_loop.TradingLoop(agent, client)
	loop.run()
