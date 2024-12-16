import time
import csv
import threading
import subprocess
import pyautogui

from app import _ENV
from app.libraries.driver import Driver
from app.libraries.mail_temp import Mail
from app.entities.straw_pool_entity import PoolEntity

class ScraperStrawPool(threading.Thread):
	
	__imageBase	: str

	def __init__(self, driver: Driver):
		self.__driver    = driver
		self.__coords    = PoolEntity.init_entity(_ENV.coordenadas)

	def run(self):
		self.__driver.get("https://strawpoll.com/embed/Qrgew7l0Ryp")
		input("hola")