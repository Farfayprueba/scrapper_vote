import time
from app import _ENV
from typing import List
from selenium.webdriver import Firefox
from app.entities.proxy_entity import ProxyEntity

from app.libraries.driver import Driver
from app.models.proxy_model import ProxyModel
from app.libraries.proxy_service import ProxyService
from app.scraper.strawPoll import ScraperStrawPool

class Controller:

	__driversToWork = 1
	
	@classmethod
	def main(cls):
		taskes = []
		print("Iniciando proceso de bots")
		drivers = cls.__open_drivers()
		driver = drivers[f"driver_{1}"]
		proxies = cls.__get_proxys()
		proxyService = ProxyService(proxies)
		for proxy in proxies:
			proxyService.set_proxy()
			scrapper = ScraperStrawPool(driver)
			scrapper.run()
			proxyService.disable_proxy()
		for driver in drivers.values(): 
			cls.__close_driver(driver)

	@classmethod
	def __get_proxys(cls) -> List[ProxyEntity]:
		api = _ENV.enviroment.proxyapi
		proxies = ProxyModel.get_proxys(api)
		return proxies

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