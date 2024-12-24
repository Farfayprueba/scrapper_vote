import hashlib
import random
from app import _ENV

class Rut:

    @classmethod
    def digito_verificador(cls, rut):
        producto = [2,3,4,5,6,7] 
        list_rut = list(map(int, str(rut))) 
        list_rut.reverse()
        contador = 0
        pivote = 0
        for i in list_rut:
            if pivote >= len(producto):
                pivote = 0
            contador = contador+(i*producto[pivote])
            pivote += 1
        suma_dig = 11-(contador%11)
        if suma_dig == 11:
            verificador = 0
        elif suma_dig == 10:
            verificador = 'k'
        else:
            verificador = suma_dig
        return verificador

    # @classmethod
    # def genera_rut(cls):
    #     numero_base = random.randint(1000000, 99999999)
    #     def calcular_dv(numero):
    #         suma = 0
    #         multiplicador = 2
    #         for digito in reversed(str(numero)):
    #             suma += int(digito) * multiplicador
    #             multiplicador = 9 if multiplicador == 7 else multiplicador + 1
    #         resto = suma % 11
    #         dv = 11 - resto
    #         if dv == 10:
    #             return "K"
    #         elif dv == 11:
    #             return "0"
    #         else:
    #             return str(dv)
    #     dv = calcular_dv(numero_base)
    #     rut = f"{numero_base}-{dv}"
    #     return rut

    @classmethod
    def genera_rut(cls):
        numero_base = random.randint(1000000, 99999999)
        def calcular_dv(numero):
            suma = 0
            multiplicador = 2
            for digito in reversed(str(numero)):
                suma += int(digito) * multiplicador
                multiplicador = 2 if multiplicador == 7 else multiplicador + 1
            resto = suma % 11
            dv = 11 - resto
            if dv == 10:
                return "k"
            elif dv == 11:
                return "0"
            else:
                return str(dv)
        dv = calcular_dv(numero_base)
        rut = f"{numero_base}-{dv}"
        return rut

