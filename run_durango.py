from app.controllers.durango_controller import Controller
from app import _ENV
import sys

if __name__ == '__main__':
	block = _ENV.enviroment.block
	lenBlock = _ENV.enviroment.lenblock
	Controller.main(int(block), int(lenBlock))