
from app import _ENV
import threading
from selenium import webdriver
from app.libraries.driver import Driver
from app.scraper.numetika_scraper import NumetikaScraper


class NumetikaController:
	
	__driversToWork = 6
	
	@classmethod
	def main(cls):
		drivers = cls.__open_drivers()
		tasks = []
		for idx in range(1, cls.__driversToWork+1):
			task = NumetikaScraper(drivers.get(f"driver_{idx}"),idx)
			tasks.append(task)
		for task in tasks: task.start()
		for task in tasks: task.join()
		for driver in drivers.values(): cls.__close_driver(driver)
  
	
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