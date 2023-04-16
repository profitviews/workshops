# Note: this is to be used within profitview.net/trading/bots

from profitview import Link, http, logger

import numpy as np
import pandas as pd
import scipy
import talib
import threading
import time


TIME_LOOKUP = {
    '1m':  60_000,
	'15m': 60_000 * 15,
    '1h':  60_000 * 60,
    '1d':  60_000 * 60 * 24,    
}


class Trading(Link):
    
    def __init__(self):
        super().__init__()
        # ALGO PARAMS
        self.src = 'bitmex' # exchange name
        self.venue = 'BitMEX' # API key name
        self.sym = 'XBTUSD'  # symbol we will trade
        self.level = '1m' # OHLC candle granularity
        self.lookback = 150 # number of close prices 
        self.time_step = TIME_LOOKUP[self.level] # time step in milliseconds
        
        # ALGO STRATEGY STATE
        self.last = None # last price update
        self.closes = dict() # time bin -> close price
        self.macd_hist = None # current MACD histogram value
        self.macd_slope = None # current MACD histogram slope
        
        # RUN ON STARTUP
        self.on_startup()

	@property
    def time_bin_now(self):
		return self.candle_bin(self.epoch_now, self.level)
    
    # MARKET DATA STATE     
    def on_startup(self):
		self.fetch_latest_closes()
		self.fetch_current_risk()
		self.update_closes()

	def fetch_latest_closes(self):
        candles = self.fetch_candles(self.venue, sym=self.sym, level=self.level)['data']
        self.closes = {x['time']: x['close'] for x in candles}
        self.last = candles[-1]['close']		
		
	def fetch_current_risk(self):
		orders = self.fetch_open_orders('BitMEX')
		positions = self.fetch_positions('BitMEX')
        
    def update_closes(self): # update close prices every one second after each minute
        if self.last and self.time_bin_now not in self.closes:
            self.closes[self.time_bin_now] = self.last
		threading.Timer(61 - self.second, self.update_closes).start()
       
	@property
    def last_closes(self):
		start_time = self.time_bin_now - self.lookback * self.time_step
        times = [start_time + i * self.time_step for i in range(1, self.lookback)] 
        closes = np.array(pd.Series([self.closes.get(x, np.nan) for x in times]).ffill())
        return np.append(closes, [self.last])
    
    def update_signal(self):
        macd, signal, hist = talib.MACD(self.last_closes)        
        N = 10 # less points required to interpolate accurately
		try:
			cubic = scipy.interpolate.CubicSpline(range(N), hist[-N:])
			self.macd_hist = hist[-1]
			self.macd_slope = float(cubic(N-1, 1))
			logger.info((self.macd_hist, self.macd_slope))
			# self.update_position_risk()
		except Exception as e:
			logger.error(f'unable to update signal - {e}')
			
	def update_position_risk(self):
		# to complete in 3rd workshop 
		pass
			
    # TRADING EVENTS
    def order_update(self, src, sym, data):
		"""Event: receive order updates from connected exchanges"""

    def fill_update(self, src, sym, data):
		"""Event: receive trade fill updates from connected exchanges"""

    def trade_update(self, src, sym, data):
        if sym == self.sym:
            self.last = data['price']
			self.closes[self.time_bin_now] = data['price']
            self.update_signal()

