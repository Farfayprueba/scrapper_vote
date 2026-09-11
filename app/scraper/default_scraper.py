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


class ScraperDurango(threading.Thread):

	__index_target = None

	def __init__(self, driver: Driver, thread: int):
		self.__driver = driver
		threading.Thread.__init__(self, name=f'Scraper_vote_{thread}')

	def run(self):
		vote = False
		if self.__load_hotel():
			self.__fill_data()
			time.sleep(2)
			self.__submit()
			print("Voto realizado")
			time.sleep(2)
		else:
			print("no cargo nada")

	def __load_hotel(self)->bool:
		try:
			self.__driver.get("https://ee-pre-durango-mextuxgqza-uc.a.run.app/")
			time.sleep(3)
			self.__driver.execute_script("window.stop();")
			return True
		except Exception as e:
			return False

	def __fill_data(self):
		try:
			self.__fill_section_1()
			self.__fill_section_2()
			self.__fill_section_3()
			self.__fill_section_4()
			self.__fill_section_5()
			self.__fill_section_6()
			self.__fill_section_7()
			self.__fill_section_8()
			self.__fill_section_9()
			self.__fill_section_10()
			self.__fill_section_11()
			self.__fill_section_12()
			self.__fill_section_13()
			self.__fill_section_14()
			self.__fill_section_15()
			self.__fill_section_16()
			self.__fill_section_17()
		except Exception as e:
			print(e)

	def __fill_section_1(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section1 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta1"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section1)
			rows = section1.find_elements(By.CSS_SELECTOR, 'tr')
			for row in rows:
				try:
					bsoup = BeautifulSoup(row.get_attribute('outerHTML'), 'lxml')
					if 'Iván Gurrola Vega' in bsoup.text.strip():
						print(bsoup.text.strip())
						input = row.find_element(By.CSS_SELECTOR, 'input[value="Si"]')
					else:
						input = row.find_element(By.CSS_SELECTOR, 'input[value="No"]')
					self.__driver.execute_script("arguments[0].scrollIntoView();", input)
					self.__driver.execute_script("arguments[0].click();", input)
				except:
					pass
				time.sleep(1)
		except Exception as e:
			print(e)

	def __fill_section_2(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section2 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta2"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section2)
			rows = section2.find_elements(By.CSS_SELECTOR, 'tr')
			for row in rows:
				try:
					bsoup = BeautifulSoup(row.get_attribute('outerHTML'), 'lxml')
					if 'Iván Gurrola Vega' in bsoup.text.strip():
						print(bsoup.text.strip())
						input = row.find_element(By.CSS_SELECTOR, 'input[value="Muy buena"]')
					else:
						input = row.find_element(By.CSS_SELECTOR, 'input[value="Mala"]')
					self.__driver.execute_script("arguments[0].scrollIntoView();", input)
					self.__driver.execute_script("arguments[0].click();", input)
				except:
					pass
				time.sleep(1)
		except Exception as e:
			print(e)
   
	def __fill_section_3(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section3 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta3"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section3)
			try:
				input = section3.find_element(By.CSS_SELECTOR, 'input[value="Ivan Gurrola Vega"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)

	def __fill_section_4(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section4 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta4"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section4)
			try:
				input = section4.find_element(By.CSS_SELECTOR, 'input[value="Ivan Gurrola Vega"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
		
	def __fill_section_5(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section5 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta5"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section5)
			try:
				input = section5.find_element(By.CSS_SELECTOR, 'input[value="No sabe/No responde"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __fill_section_6(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section6 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta6"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section6)
			try:
				input = section6.find_element(By.CSS_SELECTOR, 'input[value="Ninguno"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __fill_section_7(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section7 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta7"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section7)
			try:
				input = section7.find_element(By.CSS_SELECTOR, 'input[value="No vota"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __fill_section_8(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section8 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta8"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section8)
			try:
				input = section8.find_element(By.CSS_SELECTOR, 'input[value="No sabe/No responde"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __fill_section_9(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section9 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta9"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section9)
			try:
				input = section9.find_element(By.CSS_SELECTOR, 'input[value="Iván Gurrola Vega"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __fill_section_10(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section10 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta10"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section10)
			try:
				input = section10.find_element(By.CSS_SELECTOR, 'input[value="MORENA"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
 
	def __fill_section_11(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section11 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta11"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section11)
			try:
				input = section11.find_element(By.CSS_SELECTOR, 'input[value="PRI"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)

	def __fill_section_12(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section12 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta12"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section12)
			try:
				input = section12.find_element(By.CSS_SELECTOR, 'input[value="No sabe/No responde"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __fill_section_13(self):
		try:
			problemas_municipio = [
				"Falta de agua potable",
				"Mal estado de las carreteras",
				"Deficiencia en la recolección de basura",
				"Inseguridad y delincuencia",
				"Acceso insuficiente a servicios de salud",
				"Escasez de empleo",
				"Deficiencia en la educación pública",
				"Ausencia de áreas recreativas y deportivas",
				"Problemas de iluminación pública",
				"Falta de transporte público eficiente",
				"Contaminación ambiental",
				"Drenaje insuficiente y riesgo de inundaciones",
				"Viviendas en mal estado",
				"Falta de acceso a internet y tecnología",
				"Incremento en los niveles de pobreza",
				"Gestión ineficiente de recursos municipales",
				"Corrupción en la administración pública",
				"Abandono de comunidades rurales",
				"Deforestación y pérdida de áreas verdes",
				"Acceso limitado a programas culturales",
				"Falta de mantenimiento en parques y plazas",
				"Carencia de programas de apoyo a pequeños negocios",
				"Aumento en el costo de los servicios básicos",
				"Contaminación de ríos y cuerpos de agua",
				"Acceso limitado a servicios para personas con discapacidad",
				"Falta de programas para el cuidado de adultos mayores",
				"Abandono de infraestructura educativa",
				"Insuficientes medidas para combatir el cambio climático",
				"Presencia de basureros clandestinos",
				"Deficiencia en la seguridad vial",
				"Problemas de movilidad urbana y tráfico vehicular",
				"Ausencia de planes de desarrollo urbano sostenible",
				"Inseguridad alimentaria en comunidades vulnerables",
				"Insuficiencia en centros de atención a la mujer",
				"Falta de incentivos para el turismo local",
				"Problemas de calidad del aire",
				"Carencia de programas de prevención contra las adicciones",
				"Pérdida de patrimonio cultural e histórico",
				"Desigualdad en el acceso a servicios básicos entre zonas urbanas y rurales",
				"Baja participación ciudadana en decisiones municipales"
			]
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section13 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta13"][class="container"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section13)
			try:
				input = section13.find_element(By.CSS_SELECTOR, 'textarea[class="form-control"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				input.send_keys(random.choice(problemas_municipio))
				time.sleep(1)
				self.__driver.execute_script("arguments[0].click();", input)
				time.sleep(1)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
      
	def __fill_section_14(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section14 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta14"][class="form-group mb-4"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section14)
			try:
				input = section14.find_element(By.CSS_SELECTOR, 'input[id="P14_edad"][class="form-control"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				input.send_keys(random.randint(20,67))
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __fill_section_15(self):
		try:
			gender = ["Mujer","Hombre"]
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section15 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta15"][class="row mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section15)
			try:
				input = section15.find_element(By.CSS_SELECTOR, f'input[value="{random.choice(gender)}"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __fill_section_16(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section16 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta16"][class="mb-3"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section16)
			try:
				inputs = section16.find_elements(By.CSS_SELECTOR, 'input[class="form-check-input"]')
				input = random.choice(inputs)
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __fill_section_17(self):
		try:
			codigo_postal_aleatorio = random.randint(34000, 35499)
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			section17 = form.find_element(By.CSS_SELECTOR,'div[id="pregunta17"][class="form-group mb-4"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", section17)
			try:
				input = section17.find_element(By.CSS_SELECTOR, 'input[id="P17_codigo_postal"][class="form-control"]')
				self.__driver.execute_script("arguments[0].scrollIntoView();", input)
				input.send_keys(codigo_postal_aleatorio)
				self.__driver.execute_script("arguments[0].click();", input)
			except:
				pass
			time.sleep(1)
		except Exception as e:
			print(e)
   
	def __submit(self):
		try:
			form  = self.__driver.find_element(By.CSS_SELECTOR, 'form[class="bg-white"][id="formulario"]')
			submitBttn = form.find_element(By.CSS_SELECTOR,'button[id="submit-btn"]')
			self.__driver.execute_script("arguments[0].scrollIntoView();", submitBttn)
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