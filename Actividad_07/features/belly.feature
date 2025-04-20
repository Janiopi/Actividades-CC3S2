# language: es

Característica: Característica del estómago

  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar en horas, minutos y segundos
    Dado que he comido 100 pepinos
    Cuando espero "2 hora, 45 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  Escenario: Comer una cantidad decimal de pepinos
    Dado que he comido 1.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: Manejar una cantidad no válida de pepinos
    Dado que he comido -5 pepinos
     Entonces error: cantidad de pepinos no válida

  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero un tiempo aleatorio entre 1 y 3 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer 1000 pepinos y esperar 10 horas
    Dado que he comido 1000 pepinos
    Cuando espero 10 horas
    Entonces mi estómago debería gruñir

  Escenario: Manejar tiempos complejos
    Dado que he comido 50 pepinos
    Cuando espero "1 hora, 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  Escenario: Comer muchos pepinos y esperar el tiempo suficiente
    Dado que he comido 15 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Saber cuántos pepinos he comido
    Dado que he comido 2 pepinos
    Cuando he comido 10 pepinos más
    Entonces debería haber comido 12 pepinos

  Escenario: Predecir si mi estómago gruñirá tras comer y esperar
    Dado que quiero predecir con 12 pepinos y 2 horas
    Entonces debería gruñir
  
  Escenario: Predecir si mi estómago gruñirá con pocos pepinos
    Dado que quiero predecir con 8 pepinos y 2 horas
    Entonces no debería gruñir

  Escenario: Ya estoy gruñendo
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Cuando pregunto cuántos pepinos más puedo comer
    Entonces debería decirme que ya no puedo comer más

  Escenario: Aún no he esperado suficiente tiempo
    Dado que he comido 8 pepinos
    Cuando espero 1 hora
    Cuando pregunto cuántos pepinos más puedo comer
    Entonces debería decirme que debo esperar más


