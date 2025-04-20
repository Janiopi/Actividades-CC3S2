import pytest
from src.belly import Belly
from unittest.mock import MagicMock


def test_comer_pepinos_fraccionarios():
    belly = Belly()
    belly.comer(2.5)
    belly.esperar(2)
    assert belly.pepinos_comidos == 2.5
    assert belly.esta_gruñendo() is False  # No pasa el umbral de 10 pepinos

def test_comer_pepinos_fraccionarios_y_gruñir():
    belly = Belly()
    belly.comer(15.25)
    belly.esperar(2)
    assert belly.esta_gruñendo() is True

def test_comer_pepinos_negativos_lanza_error():
    belly = Belly()
    with pytest.raises(ValueError):
        belly.comer(-5)

def test_grunir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True  # El estómago debe gruñir después de comer 15 pepinos y esperar 2 horas.

def test_pepinos_comidos():
    belly = Belly()
    belly.comer(2)
    belly.comer(10)
    assert belly.pepinos_comidos == 12  # Verifica que la suma de pepinos comidos sea correcta

def test_estomago_gruñendo():
    belly = Belly()
    belly.comer(15)  # Comer más de 10 pepinos
    belly.esperar(2)  # Esperar más de 1 hora
    assert belly.esta_gruñendo() == True  # El estómago debería gruñir

def test_predecir_estomago_grunira():
    belly = Belly()
    assert belly.predecir_gruñidos(12, 2) == True
    assert belly.predecir_gruñidos(8, 2) == False
    assert belly.predecir_gruñidos(15, 1) == False

def test_belly_con_reloj_mockeado():
    fake_clock = MagicMock()
    fake_clock.return_value = 9999  # Fijamos el tiempo
    belly = Belly(clock_service=fake_clock)
    belly.comer(12)
    belly.esperar(2)
    assert belly.esta_gruñendo() is True