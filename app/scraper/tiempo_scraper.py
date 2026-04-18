import threading
import time
import random
from app import _ENV
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class TiempoScraper(threading.Thread):
	
	def __init__(self, driver: Firefox, idx: int):
		self.__driver: Firefox = driver
		nameThread = f"driver_{idx}"
		threading.Thread.__init__(self, name=nameThread)
  
	def run(self):
		self.__get_url()
		self.__move_to_element()
		self.__select_target()
		self.__submit()
		
	def __get_url(self):
		try:
			self.__driver.get("https://www.tiempo.com.mx/")	
			time.sleep(5)
		except Exception as e:
			print(e)

	def __move_to_element(self):
		try:
			element = self.__driver.find_element(By.CSS_SELECTOR, "div[id='thepoll']")
			self.__driver.execute_script("arguments[0].scrollIntoView();", element)
			time.sleep(3)
		except Exception as e:
			print('Error while scrolling to element')

	def __select_target(self):
		try:
			element = self.__driver.find_element(By.CSS_SELECTOR, "input[id='radio_encuesta_18733']")
			self.__driver.execute_script('arguments[0].click();', element)
			time.sleep(2)
		except Exception as e:
			print('Error while select target')


	def __submit(self):
		try:
			submitBttn = self.__driver.find_element(By.CSS_SELECTOR, 'input[id="encuesta_votar"]')
			self.__driver.execute_script("arguments[0].click();", submitBttn)
			time.sleep(3)
		except Exception as e:
			print(e)