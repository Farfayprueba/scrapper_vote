import threading
import time
from app import _ENV
from selenium import webdriver
from selenium.webdriver.common.by import By

class ScraperChile(threading.Thread):
	
	def __init__(self, driver: webdriver, idx: int):
		self.__driver = driver
		nameThread = f"driver_{idx}"
		threading.Thread.__init__(self, name=nameThread)
  
	def run(self):
		try:
			self.__driver.get("https://docs.google.com/forms/d/e/1FAIpQLScKm74dU6fGCtbPcSM9dkGqgvm1hvs1BXathu7mRSZ34DIFmg/viewform?embedded=true")
			time.sleep(3)
			form = self.__driver.find_element(By.TAG_NAME, 'form')
			targets = form.find_elements(By.CSS_SELECTOR, 'div.nWQGrd')
			for target in targets:
				if "Marco Enríquez-Ominami" in target.text:
					submitTarget = target.find_element(By.CSS_SELECTOR, 'div.d7L4fc')
					self.__driver.execute_script("arguments[0].scrollIntoView();", target)
					self.__driver.execute_script("arguments[0].click();", submitTarget)
					time.sleep(2)
				else: 
					pass
			submitContainer = self.__driver.find_element(By.CSS_SELECTOR, 'div.lRwqcd')
			submitBttn = submitContainer.find_element(By.CSS_SELECTOR,"span.l4V7wb")
			self.__driver.execute_script("arguments[0].scrollIntoView();", submitBttn)
			self.__driver.execute_script("arguments[0].click();", submitBttn)
			time.sleep(2)
		except Exception as e:
			print(e)
  
