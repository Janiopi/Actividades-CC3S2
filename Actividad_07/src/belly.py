# src/belly.py
from src.clock import get_current_time

class Belly:
    def __init__(self, clock_service=None):
         # Cambiado a float para permitir decimales
        self.pepinos_comidos = 0.0 
        self.tiempo_esperado = 0.0 
        self.clock = get_current_time or clock_service  # Servicio de reloj para obtener el tiempo actual

    def reset(self):
        self.pepinos_comidos = 0.0
        self.tiempo_esperado = 0.0

    def comer(self, pepinos):
        if pepinos < 0 :
            raise ValueError("Cantidad de pepinos no válida. No pueden ser negativos")
        if pepinos > 1000:
            print("¡He comido demasiados pepinos! Me siento muy lleno.")
        self.pepinos_comidos += pepinos
        print(f"He comido {pepinos} pepinos.")
        

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas > 0:
            self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        # Verificar que ambas condiciones se cumplan correctamente:
        # Se han esperado al menos 1.5 horas Y se han comido más de 10 pepinos
        if round(self.tiempo_esperado, 3) >= 1.5 and self.pepinos_comidos > 10:
            return True
        return False

    def predecir_gruñidos(self,pepinos,horas):
        return horas >= 1.5 and pepinos > 10 
    
    def pepinos_restantes_para_grunir(self):
        if self.esta_gruñendo():
            return 0
        elif self.tiempo_esperado >= 1.5:
            faltan = max(0, 11 - self.pepinos_comidos)
            return faltan
        else:
            return "esperar más"
