# -*- coding: utf-8 -*-
import client.client
import agent.agent
import trading_loop

API_URL = 'https://price-stream-api.herokuapp.com/'

if __name__ == '__main__':
	agent = agent.Agent()
	client = client.Client(API_URL)
	loop = trading_loop.TradingLoop(agent, client)
	loop.run()
