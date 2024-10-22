import time
import os
import csv
import threading
import subprocess
import pyautogui

from app import _ENV
from app.libraries.mail_temp import Mail
from app.entities.pool_entity import PoolEntity

class ScraperPool(threading.Thread):
	
	__imageBase        : str

	def __init__(self, name: str, lastName: str):
		#self.__drivers        = drivers
		self.__name           = name
		self.__lastName       = lastName
		self.__imageBase      = _ENV.paths.img
		self.__mail           = None
		self.__linkValidation = None
		self.__coords    = PoolEntity.init_entity(_ENV.coordenadas)

	def run(self):

		while True:
			self.__mail = Mail.generate_mail(self.__name, self.__lastName)
			self.__linkValidation = None
			self.__open_nav()
			time.sleep(2)
			self.__load_page()
			time.sleep(3)
			if self.__verify_captcha():
				continue
			self.__login()
			time.sleep(5)
			self.__linkValidation = Mail.get_mail_link(self.__mail)
			time.sleep(3)
			self.__navigate_link(self.__linkValidation)
			for page in range(16):
				self.__click_next()
			self.__votar()
			time.sleep(1)
			#self.__clear_chrome_data()
			self.__navigate_link("chrome://settings/clearBrowserData")
			time.sleep(1)
			#pyautogui.press("enter")
			self.__click_button("eliminar")
			time.sleep(1)
			self.__close_nav()
			time.sleep(4)
			self.save_mail_to_csv(self.__mail)

	def save_mail_to_csv(self, mail):
		with open("generated_emails.csv", mode="a", newline="") as file:
			writer = csv.writer(file)
			writer.writerow([mail])
		print(f"Correo guardado en CSV: {mail}")

	def __get_available_driver(self, driverScrap:dict):
		for driver in driverScrap.values():
			url = driver.current_url
			if url == "https://www.google.com/":
				return driver

	def __click_next(self):
		try:
			pyautogui.press("right")
			time.sleep(1)
		except Exception as e:
			print(e)

	def __votar(self):
		try:
			pyautogui.click(self.__coords.voteBttn)
			time.sleep(2)
			pyautogui.click(self.__coords.voteBttnMain)
			time.sleep(1)
		except Exception as e:
			print(e)

	def __verify_captcha(self):
		if self.__validate_image("ingresar_captcha"):
			print("cerrando navegador")
			time.sleep(2)
			time.sleep(1)
			self.__close_nav()
			time.sleep(5)
			return True
		else:
			return False

	def __login(self):
		try:
			pyautogui.click(self.__coords.placeholder)
			time.sleep(1.5)
			pyautogui.press('backspace')
			time.sleep(1.5)
			user = self.__mail.split('@')
			pyautogui.write(user[0])
			time.sleep(0.5)
			pyautogui.keyDown('altright')
			pyautogui.press('q')
			pyautogui.keyUp('altright')
			time.sleep(0.5)
			pyautogui.write(user[1])
			time.sleep(1)
			self.__verify_captcha()
			self.__click_button("ingresar")
			time.sleep(3)
			pyautogui.click(self.__coords.fullName)
			pyautogui.write(self.__name)
			pyautogui.press('space')
			pyautogui.write(self.__lastName)
			self.__click_button("ingresar")
		except Exception as e:
			print(e)
			
	def __click_button(self, button: str):
		try:
			continuebttn = pyautogui.locateCenterOnScreen(self.__imageBase + '\\{image}.png'.format(image= button))
			pyautogui.moveTo(continuebttn)
			time.sleep(2)
			pyautogui.click(continuebttn)
		except Exception as e:
			print(e)

	def __open_nav(self):
		try:
			self.__process = subprocess.Popen([_ENV.paths.chrome, 'https://www.google.com.mx/?hl=es'])  # Open Chrome - Google
		except:
			pass

	def __close_nav(self):
		try:
			if os.name == 'nt':  # Para Windows
				subprocess.call("taskkill /IM chrome.exe /F", shell=True)
			else: 
				subprocess.call("pkill -f chrome", shell=True)
			print("Todos los procesos de Chrome han sido cerrados.")
		
		except Exception as e:
			print(f"Error al cerrar Chrome: {e}")
	
	def __navigate_link(self, linkDestiny:str)->bool:
		try:
			value = False
			if self.__click_link_nav():
				pyautogui.hotkey('ctrl', 'a')
				time.sleep(1.5)
				pyautogui.press('backspace')
				time.sleep(1.5)
				pyautogui.write(linkDestiny)
				time.sleep(2)
				pyautogui.press('enter')
				time.sleep(3)
				value = True
			return value
		except:
			return False
		
	def __click_link_nav(self)->bool:
		try:
			pyautogui.click(self.__coords.link)
			time.sleep(2)
			return True
		except Exception as e:
			print('Error Link Na:', e)
			return False
		
	def __load_page(self)->bool:
		try:
			self.__navigate_link("https://www.pagina7.cl/premios-cordillera/")
		except:
			return False
		
	def __validate_image(self, nameImg:str)->bool:
		try:
			value = True 
			imageAppear = pyautogui.locateOnScreen(self.__imageBase + "\\{}.png".format(nameImg))
			if imageAppear is None:
				value = False
			return value
		except:
			return False
		
	def __clear_chrome_data(self):
		try:	
			command = f'"{_ENV.paths.chrome}" --user-data-dir="%LOCALAPPDATA%\\Google\\Chrome\\User Data" --start-maximized --disable-extensions --new-window "chrome://settings/clearBrowserData"'
			subprocess.Popen(command, shell=True)
			pyautogui.press('enter')  
			time.sleep(5)
			pyautogui.hotkey('ctrl', 'shift', 'del') 
			time.sleep(2) 
			pyautogui.press('down', presses=1)
			pyautogui.press('tab')  
			pyautogui.press('enter') 
		except Exception as e:
			print(e)