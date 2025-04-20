from src.clock import get_current_time


class Belly:
    def __init__(self, clock_service=None):
        self.clock = clock_service or get_current_time
        self.pepinos_comidos = 0.0
        self.tiempo_esperado = 0.0

    def reset(self):
        self.pepinos_comidos = 0.0
        self.tiempo_esperado = 0.0

    def comer(self, pepinos):
        if pepinos < 0:
            raise ValueError(
                "Cantidad de pepinos no válida. No pueden ser negativos"
            )
        if pepinos > 1000:
            print("¡He comido demasiados pepinos! Me siento muy lleno.")
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas > 0:
            self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        tiempo_suficiente = round(self.tiempo_esperado, 3) >= 1.5
        ha_comido_mucho = self.pepinos_comidos > 10
        return tiempo_suficiente and ha_comido_mucho

    def predecir_gruñidos(self, pepinos, horas):
        return horas >= 1.5 and pepinos > 10

    def pepinos_restantes_para_grunir(self):
        if self.esta_gruñendo():
            return 0
        elif self.tiempo_esperado >= 1.5:
            return max(0, 11 - self.pepinos_comidos)
        return "esperar más"
