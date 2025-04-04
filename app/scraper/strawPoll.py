import time
import csv
import threading
import pyautogui

from app import _ENV
from app.libraries.driver import Driver
from selenium.webdriver.common.by import By
from app.entities.straw_pool_entity import PoolEntity
from app.entities.proxy_entity import ProxyEntity

class ScraperStrawPool(threading.Thread):
	
	__imageBase	: str

	def __init__(self, driver: Driver, thread: int, proxy:ProxyEntity):
		self.__driver = driver
		self.__coords = PoolEntity.init_entity(_ENV.coordenadas)
		self.__proxy  = proxy
		threading.Thread.__init__(self, name=f'Scraper_vote_{thread}')

	def run(self):
		if self.__load_hotel():
			if self.__select_vote():
				time.sleep(3)
				self.__vote()
			else:
				print("error encontrando target")
		else:
			print("no cargo nada")

	def __load_hotel(self)->bool:
		try:
			self.__driver.get("https://strawpoll.com/embed/Qrgew7l0Ryp")
			time.sleep(5)
			self.__driver.execute_script("window.stop();")
			return True
		except Exception as e:
			return False

	def __select_vote(self)->bool:
		try:
			candidates = self.__driver.find_element(By.CSS_SELECTOR,'div[x-data="imageVote"]')
			target = candidates.find_element(By.CSS_SELECTOR,'input[id="option-DwyoYmeO0gA"]')
			self.__driver.execute_script("arguments[0].click();", target)
			return True
		except:
			return False
		
	def __vote(self):
		try:
			voteButton = self.__driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
			self.__driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(1)
			self.__driver.execute_script("arguments[0].click();", voteButton)
			time.sleep(13)
		except Exception as e:
			print(e)

