from .. import _ENV
import time
from io import BytesIO
from seleniumwire import webdriver as webdriver_wire
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#import seleniumwire.undetected_chromedriver as uc

class Driver:

	@staticmethod
	def chrome():
		driver_options = webdriver.ChromeOptions()
		driver_options.add_argument('--ignore-certificate-errors')
		driver_options.add_argument('--ignore-ssl-errors')
		driver_options.add_argument('--disable-infobars')
		driver = webdriver.Chrome (
			executable_path = _ENV.driver.chrome,
			options = driver_options
		)
		driver.implicitly_wait(30)
		driver.maximize_window()
		return driver

	# @staticmethod
	# def chrome_wire():
	# 	chrome_options = uc.ChromeOptions()
	# 	driver = uc.Chrome(
	# 		executable_path = _ENV.driver.chrome,
	# 		options=chrome_options,
	# 		seleniumwire_options={}
	# 	)
	# 	driver.implicitly_wait(30)
	# 	driver.maximize_window()
	# 	return driver

	@staticmethod
	def firefox(proxy=None, cache=None):
		driver = None
		while driver == None:
			try:
				profile = webdriver.FirefoxProfile()
				profile.set_preference("browser.cache.disk.enable", False)
				profile.set_preference("browser.cache.memory.enable", False)
				profile.set_preference("browser.cache.offline.enable", False)
				profile.set_preference("network.http.use-cache", False)
				profile.set_preference("media.autoplay.default", 0)
				profile.set_preference("toolkit.cosmeticAnimations.enabled", False)
				profile.set_preference("network.predictor.enabled", False)
				profile.set_preference("app.update.enabled", False)
				profile.set_preference("extensions.update.enabled", False)
				profile.set_preference("network.cookie.cookieBehavior", 2)
				if proxy is None:
					if cache == 'disable':
						driver = webdriver.Firefox(executable_path=_ENV.driver.firefox, firefox_profile=profile)
					else:
						driver = webdriver.Firefox(executable_path=_ENV.driver.firefox)
				else:
					capabilities = DesiredCapabilities().FIREFOX
					capabilities['marionette'] = True
					proxy = '{}:{}'.format(proxy.ip, proxy.port)
					capabilities['proxy'] = {"proxyType":"MANUAL", "httpProxy":proxy, "sslProxy":proxy}		
					if cache == 'disable':
						driver = webdriver.Firefox(executable_path=_ENV.driver.firefox, capabilities=capabilities, firefox_profile=profile)
					else:
						driver = webdriver.Firefox(executable_path=_ENV.driver.firefox, capabilities=capabilities)
			except Exception as e:
				Driver.close(driver)
				driver = None
				print('ErrorOpenDriver:',e)
		driver.maximize_window()
		return driver
	
	@staticmethod
	def firefox_wire(proxy=None, cache=None):
		driver = None
		while driver == None:
			try:
				profile = webdriver.FirefoxProfile()
				#profile.set_preference("browser.cache.disk.enable", False)
				#profile.set_preference("browser.cache.memory.enable", False)
				#profile.set_preference("browser.cache.offline.enable", False)
				profile.set_preference("network.http.use-cache", False)
				profile.set_preference("media.autoplay.default", 0)
				profile.set_preference("toolkit.cosmeticAnimations.enabled", False)
				profile.set_preference("network.predictor.enabled", False)
				profile.set_preference("app.update.enabled", False)
				profile.set_preference("extensions.update.enabled", False)
				#profile.set_preference("network.cookie.cookieBehavior", 2)
				if proxy is None:
					if cache == 'disable':
						driver = webdriver.Firefox(executable_path=_ENV.driver.firefox, firefox_profile=profile)
					else:
						driver = webdriver.Firefox(executable_path=_ENV.driver.firefox)
				else:
					proxy_url = f"http://{proxy.username}:{proxy.password}@{proxy.ip}:{proxy.port}" 
					seleniumwire_options = {
					    "proxy": {
					        "http": proxy_url,
					        "https": proxy_url
					    },
					}
					if cache == 'disable':
						driver = webdriver_wire.Firefox(executable_path=_ENV.driver.firefox, seleniumwire_options=seleniumwire_options, firefox_profile=profile)
					else:
						driver = webdriver_wire.Firefox(executable_path=_ENV.driver.firefox)
			except Exception as e:
				Driver.close(driver)
				driver = None
				print('ErrorOpenDriver:',e)
		driver.maximize_window()
		return driver

	@staticmethod
	def close(driver):
		try:
			driver.quit()
		except Exception as e:
			pass

	@staticmethod
	def close_tabs(driver):
		while len(driver.window_handles) > 1:
			driver.switch_to.window(driver.window_handles[-1])
			driver.close()
			time.sleep(0.5)
		driver.switch_to.window(driver.window_handles[0])