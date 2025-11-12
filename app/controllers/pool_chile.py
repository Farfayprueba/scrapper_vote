import time
import math
import random
from app import _ENV
from typing import List
from selenium.webdriver import Firefox
from app.entities.proxy_entity import ProxyEntity
from app.libraries.proxy_service import ProxyService
from app.libraries.driver import Driver
from app.models.proxy_model import ProxyModel
from app.scraper.scraper_chile import ScraperPoolChile

class Controller:

	__driversToWork = 5
	__proxies       : List[ProxyEntity]
	
	@classmethod
	def main(cls, block: int = 1, lenBlock: int = 1):
		taskes = []
		print("Iniciando bot de votación")
		startIteration = 1
		cls.__proxies = cls.__get_proxys(block,lenBlock)
		drivers = cls.__open_drivers()
		while True:
			cls.__init_drivers(drivers)
			taskes = []
			for driver in drivers.values():
				task = ScraperPoolChile(driver, 1)
				taskes.append(task)
			for task in taskes: task.start()
			for task in taskes: task.join()
			print(f"grupo de votos concluidos: {startIteration}")
			cls.__clear_cache(drivers)
			if startIteration % 3 == 0:
				for driver in drivers.values():
					cls.__close_driver(driver)
				drivers = cls.__open_drivers()
			startIteration += 1
			time.sleep(3)

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
		randomProxy = random.choice(cls.__proxies)
		drivers = dict()
		for d in range(1, cls.__driversToWork+1):
			drivers.__setitem__(f'driver_{d}', Driver.firefox_wire(randomProxy, cache='disable'))
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

	@classmethod
	def __clear_cache(cls, driverScrap: dict):
		for driver in driverScrap.values():
			cls.__clean_browser_cache(driver)

	@classmethod
	def __clean_browser_cache(cls, driver):
		try:
			driver.delete_all_cookies()
			driver.execute_script("window.localStorage.clear();")
			driver.execute_script("window.sessionStorage.clear();")
			driver.get("about:blank")
		except Exception as e:
			print(f"Error limpiando caché: {e}")