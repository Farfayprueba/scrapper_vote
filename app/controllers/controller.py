import time
import math
from typing import List
from datetime import timedelta, datetime
from selenium.webdriver import Firefox

from app.libraries.mail_temp import Mail
from app.scraper.scraper import ScraperPool
from app.scraper.strawPoll import ScraperStrawPool

class Controller:

	__driversToWork = 1
	
	@classmethod
	def main(cls):
		taskes = []
		print("Iniciando proceso de bots")
		scrapper = ScraperPool(name, lastName)
		scrapper.run()
		#for driver in drivers.values():
		#	cls.__close_driver(driver)
