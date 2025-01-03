import time
import math
from typing import List
from datetime import timedelta, datetime
from selenium.webdriver import Firefox

from app.libraries.driver import Driver
from app.libraries.mail_temp import Mail
from app.scraper.scraper import ScraperPool

class Controller:

	__driversToWork = 1
	
	@classmethod
	def main(cls):
		taskes = []
		print("Iniciando proceso de bots")
		name = "Isaac"
		lastName = "Perez"
		scrapper = ScraperPool(name, lastName)
		scrapper.run()
		#for driver in drivers.values():
		#	cls.__close_driver(driver)


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