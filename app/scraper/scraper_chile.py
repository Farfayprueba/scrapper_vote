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


class ScraperPoolChile(threading.Thread):
	
	__index_target = None

	def __init__(self, driver: Driver, thread: int):
		self.__driver = driver
		threading.Thread.__init__(self, name=f'Scraper_vote_{thread}')

	def run(self):
		vote = False
		if self.__load_hotel():
			self.__go_selection()
			while vote == False:
				if self.__is_target():
					self.__vote()
				else:
					self.__vote()
					if self.__validate_form():
						time.sleep(3)
						vote = True
						break
				time.sleep(1)
			self.__fill_data()
			time.sleep(2)
			self.__submit()
			time.sleep(2)
		else:
			print("no cargo nada")

	def __load_hotel(self)->bool:
		try:
			self.__driver.get("https://copihuedeoro.cl/")
			time.sleep(3)
			self.__driver.execute_script("window.stop();")
			return True
		except Exception as e:
			return False
		
	def __go_selection(self):
		try: 
			selectionsPool = self.__driver.find_element(By.CSS_SELECTOR, 'button[class="nextSectionButton"]')
			self.__driver.execute_script("arguments[0].click();", selectionsPool)
		except Exception as e:
			print(e)

	def __is_target(self):
		active = self.__driver.find_element(By.CSS_SELECTOR, 'div[class="seleccion carousel-item active"]')
		options = active.find_element(By.CSS_SELECTOR, 'div[class="container-fluid opciones"]')
		nominees = options.find_elements(By.CSS_SELECTOR, 'div[class="nominados row"] > h4')
		for idx, name in enumerate(nominees):
			if name.text == "Pangal Andrade":
				self.__index_target = idx
				return True
			else:
				pass
		return False

	def __vote(self):
		try:
			if self.__index_target:
				active = self.__driver.find_element(By.CSS_SELECTOR, 'div[class="seleccion carousel-item active"]')
				options = active.find_element(By.CSS_SELECTOR, 'div[class="container-fluid opciones"]')
				nominees = options.find_elements(By.CSS_SELECTOR, 'div[class="nominados row"] > div > label')
				actions = ActionChains(self.__driver)
				actions.move_to_element(nominees[self.__index_target]).perform()
				time.sleep(1)
				actions.reset_actions()
				self.__driver.execute_script("arguments[0].click();", nominees[self.__index_target])
			else:
				active = self.__driver.find_element(By.CSS_SELECTOR, 'div[class="seleccion carousel-item active"]')
				options = active.find_element(By.CSS_SELECTOR, 'div[class="container-fluid opciones"]')
				nominees = options.find_elements(By.CSS_SELECTOR, 'div[class="nominados row"] > div > label')
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
			form = bsoup.find('section', {'id': 'formulario', 'class': 'active'})
			return form is not None
		except Exception as e:
			print(f"Error while validating form: {e}")
			return False

	def __fill_data(self):
		try:
			nombreEnt = self.__generate_random_name()
			rut = str(Rut.genera_rut())
			mail = Mail.generate_mail(nombreEnt.nombre, f"{nombreEnt.paterno} {nombreEnt.materno}")
			nameInput = self.__driver.find_element(By.CSS_SELECTOR,'input[id="nombre"]')
			nameInput.send_keys(f"{nombreEnt.nombre} {nombreEnt.paterno} {nombreEnt.materno}")
			rutInput = self.__driver.find_element(By.CSS_SELECTOR,'input[id="rut"')
			rutInput.send_keys(rut)
			mailInput = self.__driver.find_element(By.CSS_SELECTOR,'input[id="email"')
			mailInput.send_keys(mail)
		except Exception as e:
			print(e)

	def __submit(self):
		try:
			submitBttn = self.__driver.find_element(By.CSS_SELECTOR,'button[id="carousel-encuesta-submit"]')
			self.__driver.execute_script("arguments[0].click();", submitBttn)
			time.sleep(1)
		except Exception as e:
			print(e)

	def __generate_random_name(self):
		df = pd.read_csv(_ENV.paths.nombres)
		df.columns = ['nombre', 'paterno', 'materno']
		name = nameEntity.init_entity()
		name.nombre = random.choice(df['nombre'].dropna().tolist())
		name.paterno = random.choice(df['paterno'].dropna().tolist())
		name.materno = random.choice(df['materno'].dropna().tolist())
		return name