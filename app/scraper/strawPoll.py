import time
import csv
import threading
import subprocess
import pyautogui

from app import _ENV
from app.libraries.driver import Driver
from selenium.webdriver.common.by import By
from app.entities.straw_pool_entity import PoolEntity

class ScraperStrawPool(threading.Thread):
	
	__imageBase	: str

	def __init__(self, driver: Driver, thread: int):
		self.__driver    = driver
		self.__coords    = PoolEntity.init_entity(_ENV.coordenadas)
		threading.Thread.__init__(self, name=f'Scraper_vote_{thread}')

	def run(self):
		if self.__load_hotel():
			if self.__select_vote():
				time.sleep(3)
				self.__vote()
				print("voto realizado correctamente")
			else:
				print("error encontrando target")
		else:
			print("no cargo nada")

	def __load_hotel(self)->bool:
		try:
			self.__driver.get("https://strawpoll.com/embed/Qrgew7l0Ryp")
			time.sleep(2)
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
			self.__driver.execute_script("arguments[0].click();", voteButton)
		except Exception as e:
			print(e)