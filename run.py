from app.controllers.pool_chile import Controller
from app import _ENV
import sys

if __name__ == '__main__':
	block = _ENV.enviroment.block
	lenBlock = _ENV.enviroment.lenblock
	Controller.main(int(block), int(lenBlock))

#https://drive.google.com/file/d/1wmLludIHvpD1H_pL_M_sxgUjog87LNB6/view?usp=sharing
# [ENVIROMENT]
# BLOCK = 1
# LENBLOCK = 1
# RAPPIAPI = c696be32e6msh772b555b93c01c1p18124fjsn8f77a289631c
# CAPTCHA_CLICK = 123,312
# PROXYAPI = 57o27uf39yom6txc96m0k7icuoyydoqx1b89bo03
# PROXY = True

# [DRIVER]
# CHROME = C:\Proyectos\chromedriver.exe
# FIREFOX = C:\Proyectos\geckodriver.exe

# [PATHS]
# IMG = C:\Proyectos\img\prueba
# CHROME = C:\Program Files\Google\Chrome\Application\chrome.exe
# DOWNLOADS = C:\Users\Equipo\Downloads
# NOMBRES = C:\Users\isaac.perez\Desktop\Proyectos\externals\nombres.csv

# [COORDENADAS]
# LINK = 769,64
# PLACEHOLDERMAIL = 1313,516
# INGRESARBTTN = 1365,647
# CAPTCHA = 1181,531
# FULLNAME = 1293,671
# NEXTBTTN = 1386,386
# VOTEBTTN = 376,692
# VOTEBTTNMAIN = 1062,609

# [COORDENADAS2]