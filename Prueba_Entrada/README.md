# Prueba de Entrada - Juego de Trivia

### Link del repositorio

[https://github.com/Janiopi/TriviaGame-CC3S2]

#### Día 1 - Configuración del entorno y estructura básica (Sprint 1 – Parte 1)

#### Objetivos

- **Configuración del proyecto:**
  - Crear la carpeta del proyecto y configurar el entorno virtual.
  - Instalar FastAPI, Uvicorn, asyncpg, databases y otras dependencias.
- **Docker y Docker Compose:**
  - Crear el `Dockerfile` para la aplicación.
  - Configurar el archivo `docker-compose.yml` para levantar PostgreSQL y el servicio web.
- **Inicialización en Git:**
  - Iniciar el repositorio y crear la rama `develop` junto con la rama base para la estructura.

#### Tareas y comandos Git

- Crear la estructura del proyecto:

  ```bash
  mkdir trivia-game-python
  cd trivia-game-python
  python3 -m venv venv
  source venv/bin/activate
  pip install fastapi uvicorn asyncpg databases
  ```

  ![alt text](image.png)

- Commit inicial en main

  ![alt text](image-1.png)

- Creando la rama develop y haciendo un commit dentro de ella

  ```bash
  git checkout -b  develop
  ```

  ![alt text](image-2.png)

- Crear archivos `Dockerfile` y `docker-compose.yml` con el contenido indicado.

  _INSERTAR IMAGENES DOCKERFILE Y DOCKER_COMPOSE_

- Realizar el primer commit:

  ```bash
  git add .
  git commit -m "Configuración inicial del proyecto y archivos Docker"
  ```

  ![alt text](image-3.png)

- Fusionando con la rama develop
  ![alt text](image-4.png)

- Añadiendo el tag correspondiente

  ![alt text](image-5.png)

- **Registro diario:** Utilizar `git diff` para ver los cambios y `git blame` en los archivos modificados para registrar el historial.

#### Día 2 - Implementación de la clase Question y pruebas unitarias (Sprint 1 – Parte 2)

#### Objetivos

- **Clase Question:**
  - Implementar la clase `Question` en Python para gestionar preguntas y respuestas.
- **Pruebas unitarias:**
  - Configurar pytest e implementar pruebas básicas para validar la funcionalidad de `is_correct`.

#### Tareas y comandos Git

- Crear el archivo `trivia.py` con la clase:

  ![alt text](image-6.png)

- Crear el archivo `test_trivia.py` con pruebas unitarias:
  ![alt text](image-7.png)

- Instalando pytest
  ![alt text](image-8.png)
- Ejecutar pytest para validar:
  ![alt text](image-9.png)
- Realizar commit en la rama:

  ```bash
  git add .
  git commit -m "Implementación de la clase Question y pruebas unitarias básicas"
  ```

  ![alt text](image-10.png)

- **Registro diario:** Utilizar `git diff` para ver diferencias y `git blame test_trivia.py` para asignar responsabilidad en el código.

#### Día 3 - Implementación de la clase Quiz y flujo básico del juego (Sprint 1 – Parte 3)

#### Objetivos

- **Clase Quiz:**
  - Desarrollar la clase `Quiz` para manejar el flujo del juego (añadir preguntas y obtener la siguiente).
- **Integración básica:**
  - Conectar la lógica de `Question` y `Quiz` para permitir la presentación de preguntas.
- **Gestión de ramas:**
  - Trabajar en una rama específica para la estructura básica, por ejemplo, `feature/estructura-basic`.

#### Tareas y comandos Git

- Crear la clase `Quiz` en `trivia.py`:

  ```python
  class Quiz:
      def __init__(self):
          self.questions = []
          self.current_question_index = 0

      def add_question(self, question):
          self.questions.append(question)

      def get_next_question(self):
          if self.current_question_index < len(self.questions):
              question = self.questions[self.current_question_index]
              self.current_question_index += 1
              return question
          return None
  ```

- Agregar lógica de interacción básica en una función (por ejemplo, `run_quiz()` que imprima las preguntas en consola).
- Realizar commit en la rama:
  ```bash
  git checkout -b feature/estructura-basic
  git add .
  git commit -m "Implementación de la clase Quiz y flujo básico del juego"
  ```
- **Registro diario:** Utilizar `git diff` para revisar cambios y `git checkout` para navegar entre ramas.

#### Día 4 - Sistema de puntuación, manejo de rondas y finalización del juego (Sprint 2)

#### Objetivos

- **Ampliar la clase Quiz:**
  - Incluir atributos para puntaje: `correct_answers` y `incorrect_answers`.
  - Implementar el método `answer_question` para actualizar la puntuación.
- **Manejo de rondas:**
  - Definir la lógica para las 10 rondas y la terminación del juego.
- **Pruebas unitarias:**
  - Agregar tests para validar el sistema de puntuación.

#### Tareas y comandos Git

- Modificar la clase `Quiz`:

  ```python
  class Quiz:
      def __init__(self):
          self.questions = []
          self.current_question_index = 0
          self.correct_answers = 0
          self.incorrect_answers = 0

      def add_question(self, question):
          self.questions.append(question)

      def get_next_question(self):
          if self.current_question_index < len(self.questions):
              question = self.questions[self.current_question_index]
              self.current_question_index += 1
              return question
          return None

      def answer_question(self, question, answer):
          if question.is_correct(answer):
              self.correct_answers += 1
              return True
          else:
              self.incorrect_answers += 1
              return False
  ```

- Actualizar las pruebas unitarias para incluir la verificación de la puntuación:

  ```python
  from trivia import Quiz, Question

  def test_quiz_scoring():
      quiz = Quiz()
      question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
      quiz.add_question(question)
      assert quiz.answer_question(question, "4") == True
      assert quiz.correct_answers == 1
  ```

- Implementar la función `run_quiz()` para el flujo de 10 rondas.
- Realizar commit:
  ```bash
  git add .
  git commit -m "Implementación de sistema de puntuación, manejo de rondas y finalización del juego"
  ```
- **Registro diario:** Usar `git blame` para verificar el origen de cada cambio en la clase Quiz y documentar el progreso.

#### Día 5 - Mejoras en la interfaz de usuario y refinamientos (Sprint 3)

#### Objetivos

- **Interfaz de consola:**
  - Refinar la presentación de preguntas y respuestas en la consola.
  - Agregar mensajes de bienvenida y resumen final detallado.
- **Características adicionales:**
  - Incorporar niveles de dificultad (por ejemplo, ajustar la selección de preguntas según el rendimiento).
- **Gestión de ramas:**
  - Crear una rama `feature/ui-improvements` para estos cambios y posteriormente fusionarla en `develop`.

#### Tareas y comandos Git

- Mejorar la función `run_quiz()`:
  ```python
  def run_quiz():
      print("Bienvenido al juego de Trivia!")
      print("Responde las siguientes preguntas seleccionando el número de la opción correcta.")
      quiz = Quiz()
      # Aquí se cargarán 10 preguntas, por ejemplo:
      # quiz.add_question(Question(...))
      while quiz.current_question_index < 10:
          question = quiz.get_next_question()
          if question:
              print(f"Pregunta {quiz.current_question_index}: {question.description}")
              for idx, option in enumerate(question.options):
                  print(f"{idx + 1}) {option}")
              answer = input("Tu respuesta: ")
              if quiz.answer_question(question, answer):
                  print("¡Correcto!")
              else:
                  print("Incorrecto.")
          else:
              break
      print("Juego terminado.")
      print(f"Preguntas contestadas: {quiz.current_question_index}")
      print(f"Respuestas correctas: {quiz.correct_answers}")
      print(f"Respuestas incorrectas: {quiz.incorrect_answers}")
  ```
- Realizar pruebas de la interfaz y ajustes en los mensajes.
- Crear y trabajar en la rama de mejoras:
  ```bash
  git checkout -b feature/ui-improvements
  git add .
  git commit -m "Mejoras en la interfaz de usuario y resumen final detallado"
  ```
- Revisar cambios con `git diff` y utilizar `git blame` para asegurar que cada parte del código se documente.
- Fusionar la rama en `develop`:
  ```bash
  git checkout develop
  git merge feature/ui-improvements
  ```

#### Día 6 - Pipeline CI/CD y pruebas de integración

#### Objetivos

- **CI/CD:**
  - Configurar GitHub Actions para ejecutar pruebas unitarias e integración.
  - Incluir análisis de código estático (SonarQube/SonarCloud) y pruebas de integración para la API de FastAPI.
- **Pruebas de integración:**
  - Implementar pruebas de integración utilizando httpx y TestClient de FastAPI.
- **Documentación del pipeline:**
  - Crear y actualizar el archivo de workflow (por ejemplo, `.github/workflows/ci.yml`).

#### Tareas y comandos Git

- Crear el archivo `.github/workflows/ci.yml` con el siguiente contenido (adaptado a las necesidades):

  ```yaml
  name: Python CI

  on:
    push:
      branches: [develop, main]

  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: '3.9'
        - run: pip install -r requirements.txt
        - run: pytest
        - name: SonarQube Scan
          uses: sonarsource/sonarqube-scan-action@v1
          env:
            SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          with:
            args: >
              -Dsonar.projectKey=trivia-game-python 
              -Dsonar.sources=.
  ```

- Agregar pruebas de integración (por ejemplo, en `tests/integration/test_api.py`):

  ```python
  from fastapi.testclient import TestClient
  from main import app

  client = TestClient(app)

  def test_create_question():
      response = client.post("/questions/", json={
          "description": "What is 2 + 2?",
          "options": ["1", "2", "3", "4"],
          "correct_answer": "4"
      })
      assert response.status_code == 201
  ```

- Realizar commit:
  ```bash
  git checkout -b feature/ci-cd-integration
  git add .
  git commit -m "Configuración de pipeline CI/CD y pruebas de integración"
  ```
- **Registro diario:** Utilizar `git diff` para confirmar la correcta integración del pipeline y documentar cada cambio.

#### Día 7 - Gestión de configuración, seguridad y pruebas de rendimiento

#### Objetivos

- **Gestión de variables de entorno:**
  - Implementar un archivo `.env` para gestionar las credenciales sensibles.
  - Ajustar la aplicación para cargar configuraciones mediante `dotenv`.
- **Seguridad:**
  - Agregar pruebas automatizadas de seguridad con Bandit.
- **Pruebas de carga:**
  - Configurar pruebas de rendimiento utilizando Locust.
- **Revisión final:**
  - Validar que la cobertura de código supere el 90%.
  - Preparar documentación final y realizar el merge final a `main` con tagging.

#### Tareas y comandos Git

- Crear un archivo `.env` con:
  ```env
  DATABASE_URL=postgresql://user:password@db:5432/trivia_db
  SECRET_KEY=mysecretkey
  ```
- Modificar la aplicación para cargar variables:

  ```python
  from dotenv import load_dotenv
  import os

  load_dotenv()
  DATABASE_URL = os.getenv("DATABASE_URL")
  SECRET_KEY = os.getenv("SECRET_KEY")
  ```

- Agregar pruebas de seguridad con Bandit en el pipeline:
  ```yaml
  - name: Run Security Scan
    run: bandit -r .
  ```
- Crear archivo `locustfile.py` para pruebas de carga:

  ```python
  from locust import HttpUser, task

  class TriviaUser(HttpUser):
      @task
      def play_trivia(self):
          self.client.get("/play")
  ```

- Realizar commit final y tagging:
  ```bash
  git checkout develop
  git merge feature/ci-cd-integration
  git merge feature/ui-improvements
  git merge feature/estructura-basic
  # Asegurarse de que todos los cambios están integrados en develop
  git checkout main
  git merge develop
  git tag -a v1.0 -m "Versión final del proyecto Trivia con CI/CD y pruebas de seguridad"
  git push --follow-tags
  ```
- **Registro diario:** Utilizar `git diff` y `git blame` para revisar todos los cambios realizados, y documentar cada ejercicio y ajuste final en el repositorio.

#### Consideraciones finales

- **Documentación:** Cada commit diario y el historial del repositorio deben evidenciar el avance del proyecto; se recomienda incluir comentarios en los commits que expliquen el propósito del cambio.
- **Uso de Git:** Se debe hacer uso intensivo de comandos como:
  - `git diff` para visualizar diferencias.
  - `git blame` para rastrear la autoría de las líneas.
  - `git checkout` y ramas para gestionar funcionalidades.
  - Tagging (`git tag`) para marcar versiones importantes.

El repositorio debe contener los avances diarios (commits) que demuestren el trabajo progresivo y no únicamente la versión final.

#### **Entrega**

1. **Ramas diarias:**  
   Crea una rama específica para cada día (por ejemplo, `feature/dia1`, `feature/dia2`, …, `feature/dia7`). Trabaja en cada rama durante el día y, al final, realiza un merge a la rama principal de desarrollo (por ejemplo, `develop`).

2. **Commits bien documentados:**  
   Realiza commits frecuentes durante el día con mensajes claros que reflejen los avances (por ejemplo, "Día 3: Implementación de la clase Quiz y flujo básico"). Esto permite rastrear fácilmente cada cambio usando `git log` o `git blame`.

3. **Uso de tags:**  
   Al finalizar cada día, asigna un tag que identifique el avance diario, por ejemplo:

   ```bash
   git tag -a v1.0-day1 -m "Avance Día 1: Configuración inicial y Dockerfiles"
   git tag -a v1.0-day2 -m "Avance Día 2: Clase Question y pruebas unitarias"
   ```

4. **CHANGELOG o archivo de registro:**  
   Incluye un archivo `CHANGELOG.md` donde resumas las actividades realizadas cada día, referenciando commits, ramas o tags específicos. Esto facilita una visión global del progreso.

5. **Subida final a GitHub:**  
   Una vez que se hayan integrado todos los avances en la rama `develop` y, posteriormente, se haya hecho el merge a `main`, al subir el repositorio a GitHub el instructor podrá:
   - **Revisar el historial de commits:** Con `git log` se evidenciarán los commits diarios y sus mensajes.
   - **Ver las ramas:** Las ramas diarias (`feature/dia1`, etc.) quedarán registradas en el repositorio, o bien se documentará en el `CHANGELOG.md` cómo se realizaron los merges.
   - **Consultar los tags:** Al listar los tags (con `git tag`), se podrán identificar rápidamente los hitos diarios.

> Sube esta tarea en tu repositorio personal en una carpeta que se llama `Prueba_entrada_CC3S2` y entrega el URL de ese repositorio en la plataforma del curso.
