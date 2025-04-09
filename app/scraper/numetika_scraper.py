import threading
import time
import random
from app import _ENV
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class NumetikaScraper(threading.Thread):
	
	def __init__(self, driver: webdriver, idx: int):
		self.__driver = driver
		nameThread = f"driver_{idx}"
		threading.Thread.__init__(self, name=nameThread)
  
	def run(self):
		self.__get_url()
		self.__select_gender()
		self.__select_age()
		self.__select_ocupation()
		self.__select_municipio()
		self.__pregunta1()
		self.__pregunta2()
		self.__pregunta3()
		self.__pregunta4()
		self.__pregunta5()
		self.__pregunta6()
		self.__pregunta7()
		self.__preguntas_restantes()
		self.__pregunta15()
		self.__submit()
		
	def __get_url(self):
		try:
			self.__driver.get("https://numetika.online/gubernatura/estudio-preferencias-voto-2027.php?utm_source=facebook&utm_medium=social&utm_campaign=compartir")	
			time.sleep(5)
		except Exception as e:
			print(e)

	def __select_gender(self):
		try:
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			sectionGender = form.find_element(By.CSS_SELECTOR, 'section[id="genero"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", sectionGender)
			elements = sectionGender.find_elements(By.CSS_SELECTOR, 'div.radio label')
			gender = random.choice(elements)
			self.__driver.execute_script("arguments[0].click();", gender)
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __select_age(self):
		try:
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			sectionAge = form.find_element(By.CSS_SELECTOR, 'section[id="edad"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", sectionAge)
			elements = sectionAge.find_elements(By.CSS_SELECTOR, 'div.radio label')
			gender = random.choice(elements)
			self.__driver.execute_script("arguments[0].click();", gender)
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __select_ocupation(self):
		try:
			time.sleep(1)
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			sectionOcupation = form.find_element(By.CSS_SELECTOR, 'section[id="ocupaciones"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", sectionOcupation)
			ocupationSelect = sectionOcupation.find_element(By.CSS_SELECTOR, 'div.select select')
			time.sleep(1)
			select = Select(ocupationSelect)
			options = select.options
			selected_option = random.choice(options)
			select.select_by_visible_text(selected_option.text)
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __select_municipio(self):
		try:
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			sectionMunicipio = form.find_element(By.CSS_SELECTOR, 'section[id="municipio"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", sectionMunicipio)
			ocupationSelect = sectionMunicipio.find_element(By.CSS_SELECTOR, 'div.select select')
			select = Select(ocupationSelect)
			options = select.options
			selected_option = random.choice(options)
			select.select_by_visible_text(selected_option.text)
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __pregunta1(self):
		try:
			time.sleep(1)
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			section = form.find_element(By.CSS_SELECTOR, 'section[id="pregunta01"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section)
			selected = section.find_element(By.CSS_SELECTOR, 'label[for="RadioGroup01_2"]')
			self.__driver.execute_script("arguments[0].click();", selected)
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __pregunta2(self):
		try:
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			section = form.find_element(By.CSS_SELECTOR, 'section[id="pregunta02"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section)
			selected = section.find_element(By.CSS_SELECTOR, 'label[for="RadioGroup02_1"]')
			self.__driver.execute_script("arguments[0].click();", selected)
		except Exception as e:
			print(e)
   
	def __pregunta3(self):
		try:
			time.sleep(1)
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			section = form.find_element(By.CSS_SELECTOR, 'section[id="pregunta03"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section)
			selected = section.find_element(By.CSS_SELECTOR, 'label[for="RadioGroup03_1"]')
			self.__driver.execute_script("arguments[0].click();", selected)
		except Exception as e:
			print(e)
   
	def __pregunta4(self):
		try:
			time.sleep(1)
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			section = form.find_element(By.CSS_SELECTOR, 'section[id="pregunta04"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section)
			selected = section.find_element(By.CSS_SELECTOR, 'label[for="RadioGroup04_1"]')
			self.__driver.execute_script("arguments[0].click();", selected)
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __pregunta5(self):
		try:
			time.sleep(1)
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			section = form.find_element(By.CSS_SELECTOR, 'section[id="pregunta05"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section)
			selected = section.find_element(By.CSS_SELECTOR, 'label[for="RadioGroup05_2"]')
			self.__driver.execute_script("arguments[0].click();", selected)
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __pregunta6(self):
		try:
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			section = form.find_element(By.CSS_SELECTOR, 'section[id="pregunta06"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section)
			selected = section.find_element(By.CSS_SELECTOR, 'label[for="RadioGroup06_1"]')
			self.__driver.execute_script("arguments[0].click();", selected)
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __pregunta7(self):
		try:
			time.sleep(1)			
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			section = form.find_element(By.CSS_SELECTOR, 'section[id="pregunta07"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section)
			selected = section.find_element(By.CSS_SELECTOR, 'label[for="RadioGroup07_3"]')
			self.__driver.execute_script("arguments[0].click();", selected)
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __preguntas_restantes(self):
		preguntas = ['08','09','10','11','12','13','14']
		for idx in preguntas:
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			sectionTag = f'section[id="pregunta{idx}"]'
			section = form.find_element(By.CSS_SELECTOR, sectionTag)
			self.__driver.execute_script("arguments[0].scrollIntoView();", section)
			options = section.find_elements(By.TAG_NAME, 'label')
			for option in options:
				if "Ninguno" in option.text:
					selected = option
					break
			time.sleep(1)
			self.__driver.execute_script("arguments[0].click();", selected)
   
	def __pregunta15(self):
		try:
			time.sleep(1)			
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			section = form.find_element(By.CSS_SELECTOR, 'section[id="pregunta15"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section)
			elements = section.find_elements(By.CSS_SELECTOR, 'div.radio label')
			optionSelected = random.choice(elements)
			self.__driver.execute_script("arguments[0].click();", optionSelected)
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __submit(self):
		try:
			form = self.__driver.find_element(By.CSS_SELECTOR, 'form[id="form1"]')
			section = form.find_element(By.CSS_SELECTOR, 'section[id="boton_enviar"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section)
			selected = section.find_element(By.CSS_SELECTOR, 'input[id="submit"]')
			self.__driver.execute_script("arguments[0].click();", selected)
			time.sleep(3)
		except Exception as e:
			print(e)