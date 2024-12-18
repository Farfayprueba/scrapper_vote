import time
import math
from app import _ENV
from typing import List
from selenium.webdriver import Firefox
from selenium import webdriver
from app.entities.proxy_entity import ProxyEntity

from app.libraries.driver import Driver
from app.models.proxy_model import ProxyModel
from app.libraries.proxy_service import ProxyService
from app.scraper.strawPoll import ScraperStrawPool

class Controller:

	__driversToWork = 1
	
	@classmethod
	def main(cls, block: int = 1, lenBlock: int = 1):
		taskes = []
		print(f"Iniciando proceso de bots {block} de {lenBlock}")
		proxies = cls.__get_proxys(block, lenBlock)
		proxyService = ProxyService(proxies)
		for idx, proxy in enumerate(proxies):
			#proxyService.set_proxy()
			driver = Driver.firefox(proxy= proxy,cache='disable')
			scrapper = ScraperStrawPool(driver,idx)
			scrapper.start()
			scrapper.join()
			#proxyService.disable_proxy()
			cls.__close_driver(driver)

	@classmethod
	def __get_proxys(cls,block:int, lenBlock:int) -> List[ProxyEntity]:
		api = _ENV.enviroment.proxyapi
		proxies = ProxyModel.get_proxys(api)
		if lenBlock == 1: return proxies
		increase = math.ceil(len(proxies)/lenBlock)
		proxies = [proxies[i:i + increase] for i in range(0, len(proxies), increase)]
		return proxies[block-1]

	@classmethod
	def __open_drivers(cls)->dict:
		drivers = dict()
		for d in range(1, cls.__driversToWork+1):
			drivers.__setitem__(f'driver_{d}', Driver.firefox(cache='disable'))
		return drivers
	
	@classmethod
	def __close_driver(cls, driver: Firefox):
		try:
			driver.close()
			driver.quit()
		except Exception as e:
			print(e)

	@classmethod
	def __init_drivers(cls, driverScrap:dict):
		for driver in driverScrap.values():
			driver.get("https://www.google.com/")