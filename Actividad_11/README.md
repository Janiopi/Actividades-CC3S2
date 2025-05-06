### Actividad: Escribir aserciones en pruebas con pytest

En esta actividad aprenderás cómo escribir aserciones de pruebas utilizando pytest y otros complementos actualizados.

**Objetivos de aprendizaje**

Después de completar esta actividad, serás capaz de:

- Ejecutar casos de prueba con pytest
- Identificar los casos de prueba que fallan
- Escribir pruebas unitarias utilizando aserciones
- Generar informes de cobertura usando pytest-cov

**Paso 1: Instalación de pytest y pytest-cov**

Comencemos instalando las herramientas necesarias. En lugar de usar nosetests, utilizaremos pytest para ejecutar pruebas y pytest-cov para generar informes de cobertura de código.

En tu terminal, ejecuta el siguiente comando:

```
python3 -m pip install pytest pytest-cov
```

- Creando un entorno virtual e instalando las dependencias necesarias
  ![alt text](screnshots/image.png)

**Paso 2: Archivos de prueba**

Usaremos dos archivos para esta actividad: `stack.py` y `test_stack.py`.

- `stack.py`: Contiene la implementación de una pila (stack) que queremos probar.
- `test_stack.py`: Contiene el esqueleto de las pruebas para los métodos `push()`, `pop()`, `peek()`, y `is_empty()`.

Antes de escribir los casos de prueba, revisemos los métodos de la clase `Stack`:

```python
class Stack:
    def push(self, data: Any) -> None:
        ...
    def pop(self) -> Any:
        ...
    def peek(self) -> Any:
        ...
    def is_empty(self) -> bool:
        ...
```

Descripción de funciones:

- `push()`: Añade un elemento a la parte superior de la pila.
- `pop()`: Elimina y devuelve el elemento en la parte superior de la pila.
- `peek()`: Devuelve el valor del elemento en la parte superior de la pila sin eliminarlo.
- `is_empty()`: Devuelve True si la pila está vacía y False si no lo está.

Ten en cuenta que todos los métodos, excepto `is_empty()`, operan sobre el elemento que se encuentra en la parte superior de la pila. Por lo tanto, para que tus casos de prueba sean exhaustivos, debe haber dos o más elementos en la pila para garantizar que esté manipulando el elemento superior y no el inferior.

Puedes verificar al inicio de que las pruebas no pasan con pytest:

```
pytest -v
```

![alt text](screnshots/image-2.png)

En pytest, puedes usar la opción `-x` o `--exitfirst` para detener la ejecución de las pruebas al encontrar el primer fallo.

```
pytest -x
```

o

```
pytest --exitfirst
```

![alt text](screnshots/image-1.png)

**Observación**: [Nose](https://pypi.org/project/nose/) ejecuta las pruebas en un orden pseudoaleatorio. Esto es para garantizar que los casos de prueba no afecten el orden de ejecución ni dependan de él para funcionar.

pytest no ejecuta las pruebas en un orden pseudoaleatorio por defecto. En pytest, el orden de ejecución de las pruebas sigue la secuencia en la que se encuentran en los archivos de prueba. Es decir, las pruebas se ejecutan en el mismo orden en que están definidas dentro de cada archivo de prueba.

Sin embargo, si deseas ejecutar las pruebas en un orden aleatorio, pytest ofrece un plugin llamado pytest-randomly, que permite que las pruebas se ejecuten en un orden aleatorio o pseudoaleatorio, garantizando que los casos de prueba no dependan del orden de ejecución.

```
pytest --random-order
```

![alt text](screnshots/image-3.png)

**Paso 3: Escribiendo aserciones para el método `is_empty()`**

Vamos a comenzar con la prueba del método `is_empty()`. Este método devuelve True si la pila está vacía y False si no lo está.

Modifica la función `test_is_empty()` en `test_stack.py` para que se vea así:

![alt text](screnshots/image-6.png)

Comprueba con este código tambien:

![alt text](screnshots/image-4.png)

**Paso 4: Ejecuta pytest para verificar `is_empty()`**

Ejecuta pytest para verificar si la prueba del método `is_empty()` pasa:

```
pytest -v
```

![alt text](screnshots/image-7.png)

Si la prueba pasa, verás que `is_empty()` ha pasado. Si no, revisa el código para asegurar que la lógica de la prueba es correcta.

**Paso 5: Escribiendo aserciones para el método `peek()`**

El siguiente método que vamos a probar es `peek()`. Este método devuelve el valor en la parte superior de la pila sin eliminarlo.

Modifica la función `test_peek()` en `test_stack.py` de la siguiente manera:

![alt text](screnshots/image-8.png)

Comprueba con este código tambien:

![alt text](screnshots/image-9.png)

**Paso 6: Escribiendo aserciones para el `método pop()`**

El método `pop()` elimina y devuelve el valor en la parte superior de la pila. Para asegurarte de que la prueba es útil, debes agregar al menos dos valores a la pila.

Modifica la función `test_pop()` en `test_stack.py`:

![alt text](screnshots/image-10.png)

**Paso 7: Escribiendo aserciones para el `método push()`**

Finalmente, vamos a probar el método `push()`, que añade un valor a la pila.

Modifica la función `test_push()` en `test_stack.py`:

![alt text](screnshots/image-11.png)

**Paso 8: Ejecuta pytest para verificar todas las pruebas**
Ejecuta pytest nuevamente para asegurarte de que todas las pruebas pasan:

```
pytest -v
```

![alt text](screnshots/image-12.png)

Si todo está correcto, todas las pruebas deberían pasar y la salida mostrará resultados exitosos.

**Paso 9: Agregando cobertura de pruebas con pytest-cov**

Para asegurarte de que tus pruebas cubren suficiente código, puedes generar un informe de cobertura utilizando pytest-cov. Ejecuta el siguiente comando para generar un informe de cobertura:

```
pytest --cov=stack --cov-report term-missing
```

Esto te mostrará cuántas líneas de código están cubiertas por las pruebas y cuáles no.

![alt text](screnshots/image-13.png)

**setup.cfg**

Este es un archivo de configuración para pytest y coverage, que personaliza cómo se ejecutan las pruebas y cómo se recopila el informe de cobertura de código.

- `[tool:pytest]` Esto indica que las configuraciones que siguen son para la herramienta pytest, el marco de pruebas en Python.

- `addopts = -v --tb=short --cov=stack --cov-report=term-missing`
  - `-v`: Ejecuta pytest en modo detallado (verbose mode), lo que proporciona información adicional sobre qué pruebas están siendo ejecutadas y sus resultados.
  - `--tb=short`: Muestra solo el rastro de la pila acortado (short traceback) cuando se produce un error. Esto es útil para evitar la salida excesiva de texto en caso de errores o fallos de pruebas.
  - `--cov=stack`: Indica que pytest debe calcular la cobertura de código para el módulo o archivo stack.py. stack es el nombre del archivo o paquete para el cual se recopilará la cobertura.
  - `--cov-report=term-missing`: Muestra el informe de cobertura en la terminal e incluye las líneas faltantes que no están siendo cubiertas por las pruebas. Esto es útil para identificar qué partes del código no han sido probadas.
- `[coverage:run]` Este bloque contiene configuraciones específicas para el comando coverage run, que ejecuta las pruebas y recopila datos de cobertura.

  - `branch = True`: Esta opción indica que el análisis de cobertura debe incluir la cobertura de ramas (branch coverage), no solo de líneas de código. Esto asegura que se analicen todas las ramas condicionales (por ejemplo, si tienes un if en tu código, se verifica si ambas ramas —verdadera y falsa— han sido cubiertas por las pruebas).
  - `omit =`: Este parámetro especifica qué archivos o directorios omitir del informe de cobertura. En este caso:

    - _/tests/_: Omite cualquier archivo o directorio bajo un directorio llamado tests.
    - \_/test\_\_: Omite archivos que comiencen con test\_. Esto es útil para excluir los propios archivos de prueba del análisis de cobertura, ya que no es necesario incluirlos en el informe de cobertura de código.

- `[coverage:report]`Este bloque define cómo se debe generar el informe de cobertura de código después de ejecutar las pruebas.

  - `show_missing = True` Esta opción asegura que el informe muestre qué líneas de código están faltando en la cobertura, es decir, aquellas que no fueron ejecutadas por las pruebas. Esto te ayuda a identificar fácilmente las partes del código que no han sido probadas y donde podrías necesitar agregar más casos de prueba.

Este tipo de configuración es útil para obtener información clara sobre qué partes del código han sido probadas, y al mismo tiempo te permite ver qué partes del código aún requieren más cobertura de pruebas.

- Finalmente ejecutando pytest con el setup.cfg
  ![alt text](image.png)
