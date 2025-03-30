from app import _ENV
import threading
from selenium import webdriver
from app.libraries.driver import Driver
from app.scraper.presidential_pool_scraper import ScraperChile

class Controller:

	__driversToWork = 5
	
	@classmethod
	def main(cls):
		iteration = 0
		drivers = cls.__open_drivers()
		while True :
			tasks = []
			for idx in range(1,cls.__driversToWork+1):
				task = ScraperChile(drivers.get(f'driver_{idx}'),  idx)
				tasks.append(task)
			for task in tasks: task.start()
			for task in tasks: task.join()
			iteration += 1
			if iteration % 10 == 0:
				for driver in drivers.values():
					cls.__close_driver(driver)
				drivers = cls.__open_drivers()
			
	@classmethod
	def __open_drivers(cls)->dict:
		drivers = dict()
		for d in range(1, cls.__driversToWork+1):
			drivers.__setitem__(f'driver_{d}', Driver.firefox(cache='disable'))
		return drivers

	@classmethod
	def __close_driver(cls, driver: webdriver):
		try:
			driver.close()
			driver.quit()
		except Exception as e:
			print(e)