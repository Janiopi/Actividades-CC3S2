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

  ![alt text](image-11.png)

  ![alt text](image-12.png)

- Agregar lógica de interacción básica en una función (por ejemplo, `run_quiz()` que imprima las preguntas en consola).
  ![alt text](image-13.png)

![alt text](image-14.png)

- Realizar commit en la rama:

  ```bash
  git checkout -b feature/estructura-basic
  git add .
  git commit -m "Implementación de la clase Quiz y flujo básico del juego"
  ```

  ![alt text](image-15.png)
  ![alt text](image-16.png)

- Haciendo merge en la rama develop
  ![alt text](image-17.png)

- Añadiendo tag correspondiente
  ![alt text](image-18.png)

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

- Actualizar las pruebas unitarias para incluir la verificación de la puntuación:

  ![alt text](image-19.png)

  ![alt text](image-20.png)

- Implementar la función `run_quiz()` para el flujo de 10 rondas.
  ![alt text](image-21.png)

- Realizar commit:
  ```bash
  git add .
  git commit -m "Implementación de sistema de puntuación, manejo de rondas y finalización del juego"
  ```

![alt text](image-22.png)

![alt text](image-23.png)

- Añadiendo el tag correspondiente  
  ![alt text](image-24.png)

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
  ![alt text](image-25.png)

  Se refactorizo varias funciones. La funcion run_menu se ejecuta primero
  ![alt text](image-26.png)

  En esta se llama a get_questions_by_difficulty, la cual hace una query a la base de datos
  ![alt text](image-27.png)

- Realizar pruebas de la interfaz y ajustes en los mensajes.
  ![alt text](image-28.png)

  ![alt text](image-29.png)

- Crear y trabajar en la rama de mejoras:

  ```bash
  git checkout -b feature/ui-improvements
  git add .
  git commit -m "Mejoras en la interfaz de usuario y resumen final detallado"
  ```

  ![alt text](image-30.png)

- Revisar cambios con `git diff` y utilizar `git blame` para asegurar que cada parte del código se documente.
- Fusionar la rama en `develop`:

  ```bash
  git checkout develop
  git merge feature/ui-improvements
  ```

  ![alt text](image-31.png)

- Añadiendo el tag correspondiente
  ![alt text](image-32.png)

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

- Agregar pruebas de integración (por ejemplo, en `tests/integration/test_api.py`):

  ![alt text](image-33.png)
  (De momento solo tenemos 2 enpoints)

- Crear el archivo `.github/workflows/ci.yml` con el siguiente contenido (adaptado a las necesidades):

  ```yaml
    name: CI/CD Workflow

  on:
    push:
      branches:
        - develop
    pull_request:
      branches:
        - develop

  jobs:
    build:
      runs-on: ubuntu-latest

      steps:
        # Checkout the repository
        - name: Checkout repository
          uses: actions/checkout@v2

        # Set up Python
        - name: Set up Python 3.11
          uses: actions/setup-python@v2
          with:
            python-version: 3.11

        # Install dependencies
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt

        # Set PYTHONPATH as environment variable for the job
        - name: Set PYTHONPATH
          run: echo "PYTHONPATH=$(pwd)/app:$PYTHONPATH" >> $GITHUB_ENV
        # Run unit tests
        - name: Run unit tests
          run: |
            pytest app/test/unit

        # Run integration tests
        #      - name: Run integration tests
        #        run: |
        #          pytest app/test/integration
        # Run SonarCloud Analysis
        - name: SonarCloud Scan
          uses: sonarsource/sonarqube-scan-action@v5.0.0
          with:
            args: >
              -Dsonar.organization=janiopi
              -Dsonar.projectKey=Janiopi_TriviaGame-CC3S2
              -Dsonar.projectName=TriviaGame-CC3S2
          env:
            SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
  ```

- Tag correspondiente
  ![alt text](image-35.png)

- Realizar commit:
  ![alt text](image-34.png)
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

![alt text](image-37.png)
Utilizamos las variables de entorno para la conexión a la bd

- Agregar pruebas de seguridad con Bandit en el pipeline:

  Resultados del análisis
  ![alt text](image-36.png)

- Crear archivo `locustfile.py` para pruebas de carga:

  ```python
  from locust import HttpUser, task

  class TriviaUser(HttpUser):
      @task
      def play_trivia(self):
          self.client.get("/play")
  ```

  (No se implementó en el proyecto)

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
