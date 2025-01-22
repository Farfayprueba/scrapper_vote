import time
import math
import random
import pyautogui
from app import _ENV
from typing import List
from selenium.webdriver import Firefox
from app.entities.proxy_entity import ProxyEntity
from app.libraries.proxy_service import ProxyService
from app.libraries.driver import Driver
from app.models.proxy_model import ProxyModel
from app.scraper.scraper_durango import ScraperDurango

class Controller:

	__driversToWork = 1
	
	@classmethod
	def main(cls, block: int = 1, lenBlock: int = 1):
		taskes = []
		print(f"Iniciando proceso de bots {block} de {lenBlock}")
		proxys = cls.__get_proxys(block,lenBlock)
		while True:
			randomProxy = random.choice(proxys)
			print(randomProxy)
			drivers = cls.__open_drivers(randomProxy)
			taskes = []
			for driver in drivers.values():
				task = ScraperDurango(driver, 1)
				taskes.append(task)
			for task in taskes: task.start()
			for task in taskes: task.join()
			for driver in drivers.values():
				cls.__close_driver(driver)
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
	def __open_drivers(cls, proxy: ProxyEntity = None)->dict:
		drivers = dict()
		for d in range(1, cls.__driversToWork+1):
			drivers.__setitem__(f'driver_{d}', Driver.firefox_wire(proxy, cache='disable'))
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

	@staticmethod
	def __enter_proxy_auth(proxy):
		time.sleep(10)
		pyautogui.typewrite(proxy.user)
		pyautogui.press('tab')
		pyautogui.typewrite(proxy.password)
		pyautogui.press('enter')