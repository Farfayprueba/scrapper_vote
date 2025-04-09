
from app import _ENV
from typing import List
import math
import threading
from selenium import webdriver
from app.libraries.driver import Driver
from app.scraper.numetika_scraper import NumetikaScraper
from app.models.proxy_model import ProxyModel
from app.libraries.proxy_service import ProxyService
from app.entities.proxy_entity import ProxyEntity

class NumetikaController:
	
	__driversToWork = 6
	
	@classmethod
	def main(cls, block: int = 1, lenBlock: int = 1):
		while True:
			proxies = cls.__get_proxys(block, lenBlock)
			for idx, proxy in enumerate(proxies):
				drivers = cls.__open_drivers(proxy)
				tasks = []
				for idx in range(1, cls.__driversToWork+1):
					task = NumetikaScraper(drivers.get(f"driver_{idx}"),idx)
					tasks.append(task)
				for task in tasks: task.start()
				for task in tasks: task.join()
				for driver in drivers.values(): cls.__close_driver(driver)
  
	@classmethod
	def __get_proxys(cls,block:int, lenBlock:int) -> List[ProxyEntity]:
		api = _ENV.enviroment.proxyapi
		proxies = ProxyModel.get_proxys(api)
		if lenBlock == 1: return proxies
		increase = math.ceil(len(proxies)/lenBlock)
		proxies = [proxies[i:i + increase] for i in range(0, len(proxies), increase)]
		return proxies[block-1]	
 
	@classmethod
	def __open_drivers(cls, proxy: ProxyEntity)->dict:
		drivers = dict()
		for d in range(1, cls.__driversToWork+1):
			drivers.__setitem__(f'driver_{d}', Driver.firefox_wire(proxy= proxy, cache='disable'))
		return drivers

	@classmethod
	def __close_driver(cls, driver: webdriver):
		try:
			driver.close()
			driver.quit()
		except Exception as e:
			print(e)