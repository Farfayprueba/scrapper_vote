import time
import math
from typing import List
from datetime import timedelta, datetime
from selenium.webdriver import Firefox

from app.libraries.mail_temp import Mail
from app.scraper.pool_scrapper import ScraperPool

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
