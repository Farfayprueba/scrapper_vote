import time
import pandas as pd
import threading
import random
from bs4 import BeautifulSoup

from app import _ENV
from app.entities.name_entity import nameEntity
from app.libraries.rut_generator import Rut
from app.libraries.mail_temp import Mail
from app.libraries.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException


class ScraperPoolChile(threading.Thread):
	
	__index_target : int

	def __init__(self, driver: Driver, thread: int):
		self.__driver = driver
		threading.Thread.__init__(self, name=f'Scraper_vote_{thread}')

	def run(self):
		attempts = 1
		completeVotes = False
		if self.__load_page():
			self.__go_next()
			if self.__validate_nominates():
				while completeVotes == False and attempts < 30:
					self.__index_target = None
					if self.__is_target():
						self.__vote()
					else:
						self.__vote()
						if self.__validate_form():
							time.sleep(3)
							completeVotes = True
							break
					self.__go_next()
					time.sleep(2)
					attempts += 1
				self.__fill_data()
				time.sleep(2)
				self.__go_next()
				time.sleep(2)
		else:
			print("no cargo nada")

	def __load_page(self)->bool:
		try:
			self.__driver.get("https://copihuedeoro.cl/")
			time.sleep(3)
			self.__driver.execute_script("window.stop();")
			return True
		except Exception as e:
			return False
		
	def __go_next(self):
		cssSelectors = ['[data-testid="submit-registration-button"]','[data-testid="submit-ballot-button"]', '[data-slot="button"]']
		for css in cssSelectors:
			try:
				element = self.__driver.find_element(By.CSS_SELECTOR, css)
				self.__driver.execute_script("arguments[0].removeAttribute('disabled');", element)
				time.sleep(1)
				self.__driver.execute_script("arguments[0].click();", element)
				break
			except Exception as e:
				pass		

	def __validate_nominates(self) -> bool:
		isViewNominates = False
		attemp = 0
		while not isViewNominates and attemp < 30:
			bsoup = BeautifulSoup(self.__driver.page_source, 'lxml')
			nominateCard = bsoup.select_one('button.bg-card')
			if nominateCard:
				isViewNominates = True
			time.sleep(1)
			attemp += 1
		return isViewNominates

	def __is_target(self):
		nominees = self.__driver.find_elements(By.CSS_SELECTOR, 'button.bg-card')
		for idx, card in enumerate(nominees):
			try:
				cardText = card.text.lower().strip()
				if "karen doggenweiler" in cardText:
					self.__index_target = idx
					return True
			except StaleElementReferenceException:
				continue
		return False

	def __vote(self):
		try:
			if self.__index_target is not None:
				nominees = self.__driver.find_elements(By.CSS_SELECTOR, 'button.bg-card')
				actions = ActionChains(self.__driver)
				actions.move_to_element(nominees[self.__index_target]).perform()
				time.sleep(1)
				actions.reset_actions()
				self.__driver.execute_script("arguments[0].click();", nominees[self.__index_target])
			else:
				nominees = self.__driver.find_elements(By.CSS_SELECTOR, 'button.bg-card')
				num = random.randint(0, len(nominees) - 1)
				actions = ActionChains(self.__driver)
				actions.move_to_element(nominees[num]).perform()
				time.sleep(1)
				actions.reset_actions()
				self.__driver.execute_script("arguments[0].click();", nominees[num])
		except Exception as e:
			pass

	def __validate_form(self):
		try:
			bsoup = BeautifulSoup(self.__driver.page_source, 'lxml')
			form = bsoup.select_one('form[class]')
			return form is not None
		except Exception as e:
			return False

	def __fill_data(self):
		try:
			nombreEnt = self.__generate_random_name()
			rut = str(Rut.genera_rut())
			mail = Mail.generate_mail(nombreEnt.nombre, f"{nombreEnt.paterno} {nombreEnt.materno}")
			nameInput = self.__driver.find_element(By.CSS_SELECTOR,'input[name="name"]')
			nameInput.send_keys(f"{nombreEnt.nombre} {nombreEnt.paterno} {nombreEnt.materno}")
			rutInput = self.__driver.find_element(By.CSS_SELECTOR,'input[name="rut"]')
			rutInput.send_keys(rut)
			mailInput = self.__driver.find_element(By.CSS_SELECTOR,'input[name="email"]')
			mailInput.send_keys(mail)
			time.sleep(1)
			self.__driver.execute_script('arguments[0].click();', mailInput)
			time.sleep(2)
		except Exception as e:
			pass

	def __generate_random_name(self):
		df = pd.read_csv('storage/nombres.csv')
		df.columns = ['nombre', 'paterno', 'materno']
		name = nameEntity.init_entity()
		name.nombre = random.choice(df['nombre'].dropna().tolist())
		name.paterno = random.choice(df['paterno'].dropna().tolist())
		name.materno = random.choice(df['materno'].dropna().tolist())
		return name