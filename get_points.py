import pyautogui
import time

print("Coloca el cursor en el punto deseado. Esperando 5 segundos...")
time.sleep(5)

x, y = pyautogui.position()

print(f"Posición capturada: {x},{y}")
