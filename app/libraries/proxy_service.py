import random
import subprocess
from typing import List
from dataclasses import dataclass
from .. import _ENV

@dataclass
class ProxyEntity:
	def __init__(self,proxy):
		self.ip      = proxy.get('ip')
		self.port    = 65432
		self.country = proxy.get('country').lower()
		self.city    = proxy.get('city')

@dataclass
class ProxyService:

	__country:str
	__proxies:List[ProxyEntity]
	__backup:List[ProxyEntity]
	__proxy:ProxyEntity

	def __init__(self, proxies: List[ProxyEntity]):
		self.__proxies = proxies
		self.__backup = self.__proxies.copy()
		self.__proxy = None
		
	def __get_ip(self):
		if _ENV.enviroment.proxy == 'True':
			if len(self.__proxies) == 0:
				self.__proxies = self.__backup.copy()
			i = 0 if len(self.__proxies) == 1 else random.randrange(0,len(self.__proxies)-1)
			self.__proxy = self.__proxies.pop(i)

	def set_proxy(self):
		if _ENV.enviroment.proxy == 'True':
			self.__get_ip()
			proxyText = '{}:{}'.format(self.__proxy.ip,self.__proxy.port)
			ProxyService.__set_proxy_on_off('on', self.__proxy.ip, self.__proxy.port)
			print("Conexión por proxy activada. Proxy:",proxyText)

	def disable_proxy(self):
		if _ENV.enviroment.proxy == 'True':
			proxyText = '{}:{}'.format(self.__proxy.ip,self.__proxy.port)
			ProxyService.__set_proxy_on_off('off', self.__proxy.ip, self.__proxy.port)
			print("Conexión por proxy desactivada")

	@staticmethod
	def __set_proxy_on_off(option:str, proxyIp:str, proxyPort:str):
		if option == 'on':
			script = f"""
			$proxyServer = '{proxyIp}:{proxyPort}'
			Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyEnable -Value 1
			Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyServer -Value $proxyServer
			"""
		elif option == 'off':
			script = """
			Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyEnable -Value 0
			"""
		subprocess.run(["powershell", "-Command", script], check=True)

	@staticmethod
	def set_proxy_on_off(option:str, proxyIp:str, proxyPort:str):
		if option == 'on':
			script = f"""
			$proxyServer = '{proxyIp}:{proxyPort}'
			Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyEnable -Value 1
			Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyServer -Value $proxyServer
			"""
		elif option == 'off':
			script = """
			Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyEnable -Value 0
			"""
		subprocess.run(["powershell", "-Command", script], check=True)

	def get_proxies_list(self):
		if _ENV.enviroment.proxy == 'True':
			proxyList = self.__backup
			return proxyList