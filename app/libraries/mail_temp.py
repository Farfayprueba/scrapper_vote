import hashlib
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from app import _ENV

class Mail:

    @classmethod
    def generate_mail(cls, nombres: str, apellidos: str):
        dominios = [
            "@cevipsa.com", 
            "@cpav3.com", 
            "@nuclene.com", 
            "@steveix.com", 
            "@tenvil.com", 
            "@tgvis.com", 
            "@amozix.com", 
            "@anypsd.com", 
            "@maxric.com"
        ]
        nombrecompleto = nombres.replace(" ", "")
        apellidoscompletos = apellidos.replace(" ", "")
        nombre_parts = nombres.split()
        if len(nombre_parts) >= 2:
            nombre = nombre_parts[0]
            apellido = ''.join(nombre_parts[1:])  # Une las partes restantes para formar el apellido sin espacios
        else:
            nombre = nombre_parts[0]
            apellido = ""
        now = datetime.now()
        fecha_hora = now.strftime("%H%M%S")
        email = f"{nombrecompleto.lower()}{apellidoscompletos.lower()}{fecha_hora}{random.choice(dominios)}"
        email = email.replace(" ", '')
        return email

    @classmethod
    def get_mail_link(cls, mail):
        try:
            mail_bytes = mail.encode('utf-8')
            result = hashlib.md5(mail_bytes)
            md5 = result.hexdigest()
            url = f"https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/{md5}/"
            headers = {
                "X-RapidAPI-Key": f"{_ENV.enviroment.rappiapi}",
                "X-RapidAPI-Host": "privatix-temp-mail-v1.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                for email in data:
                    mail_content = email.get("mail_text_only", "")
                    if not mail_content:  # Si no hay 'mail_text_only', buscar en el 'body'
                        mail_content = email.get("body", "")
                    soup = BeautifulSoup(mail_content, 'html.parser')
                    link_tag = soup.find('a', href=True)  # Encuentra la primera etiqueta <a> con un href
                    if link_tag and link_tag['href']:
                        link = link_tag['href']
                        return link
                print("No se encontró ningún enlace en los correos.")
            else:
                print("Error al hacer la solicitud:", response.status_code)
        except IndexError:
            print("Error: No se encontraron elementos en la lista de datos.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        

