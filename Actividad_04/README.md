# Ejercicio 1

#### Ejercicios

##### Ejercicio 1: Manejo avanzado de ramas y resolución de conflictos

**Objetivo:** Practicar la creación, fusión y eliminación de ramas, así como la resolución de conflictos que puedan surgir durante la fusión.

**Instrucciones:**

1. **Crear una nueva rama para una característica:**

   - Crea una nueva rama llamada `feature/advanced-feature` desde la rama `main`:

   ![alt text](screenshots/image.png)

2. **Modificar archivos en la nueva rama:**

   - Edita el archivo `main.py` para incluir una función adicional:

     ```python
     def greet():
         print('Hello from advanced feature')

     greet()
     ```

   - Añade y confirma estos cambios en la rama `feature/advanced-feature`:

   ![alt text](image_1.png)

3. **Simular un desarrollo paralelo en la rama main:**

   - Cambia de nuevo a la rama `main`:
     ![alt text](image-1_1.png)

   - Edita el archivo `main.py` de forma diferente (por ejemplo, cambia el mensaje del print original):
     ![alt text](image-2_1.png)
   - Añade y confirma estos cambios en la rama `main`:

     ![alt text](image-3.png)

4. **Intentar fusionar la rama feature/advanced-feature en main:**

   - Fusiona la rama `feature/advanced-feature` en `main`:

     ```bash
     $ git merge feature/advanced-feature
     ```

     ![alt text](image-5.png)

5. **Resolver el conflicto de fusión:**

   - Git generará un conflicto en `main.py`. Abre el archivo y resuelve el conflicto manualmente, eligiendo cómo combinar las dos versiones.
   - Después de resolver el conflicto, añade el archivo resuelto y completa la fusión:

![alt text](image-4.png)

![alt text](image-6.png)

6. **Eliminar la rama fusionada:**

   - Una vez que hayas fusionado con éxito y resuelto los conflictos, elimina la rama `feature/advanced-feature`:
     ![alt text](image-7.png)

#### Ejercicio 2: Exploración y manipulación del historial de commits

**Objetivo:** Aprender a navegar y manipular el historial de commits usando comandos avanzados de Git.

**Instrucciones:**

1. **Ver el historial detallado de commits:**

   - Usa el comando `git log` para explorar el historial de commits, pero esta vez con más detalle:

     ```bash
     $ git log -p
     ```

   ![alt text](image-8.png)

   - Examina las diferencias introducidas en cada commit. ¿Qué cambios fueron realizados en cada uno?

   En los dos últimos commits, se fusionaron dos ramos y se modifico el archivo Actividad_04/Actividad04.md

2. **Filtrar commits por autor:**

   - Usa el siguiente comando para mostrar solo los commits realizados por un autor específico:

     ```bash
     $ git log --author="TuNombre"
     ```

     ![alt text](image-9.png)

3. **Revertir un commit:**

   ```bash
   $ git revert HEAD
   ```

   Añadiremos un txt en blanco, haremos un commit y luego revertiremos.
   ![alt text](image-10.png)

   ![alt text](image-11.png)

   - Verifica que el commit de reversión ha sido añadido correctamente al historial.

   ![alt text](image-12.png)

   ![alt text](image-13.png)

4. **Rebase interactivo:**

   - Realiza un rebase interactivo para combinar varios commits en uno solo. Esto es útil para limpiar el historial de commits antes de una fusión.
   - Usa el siguiente comando para empezar el rebase interactivo:

     ```bash
     $ git rebase -i HEAD~3
     ```

   - En el editor que se abre, combina los últimos tres commits en uno solo utilizando la opción `squash`.
     ![alt text](image-15.png)

   ![alt text](image-16.png)

5. **Visualización gráfica del historial:**

   - Usa el siguiente comando para ver una representación gráfica del historial de commits:

     ```bash
     $ git log --graph --oneline --all
     ```

     ![alt text](image-17.png)

   - Reflexiona sobre cómo el historial de tu proyecto se visualiza en este formato. ¿Qué información adicional puedes inferir?

   Se puede observar como los commits iniciales siguen una secuencia lineal, hasta que se crea una nueva rama. Posteriormente en esa rama se realizan otros commits, hasta que es fusionada con la principal.

#### Ejercicio 3: Creación y gestión de ramas desde commits específicos

**Objetivo:** Practicar la creación de ramas desde commits específicos y comprender cómo Git maneja las referencias históricas.

**Instrucciones:**

1. **Crear una nueva rama desde un commit específico:**

   - Usa el historial de commits (`git log --oneline`) para identificar un commit antiguo desde el cual crear una nueva rama:

     ```bash
     $ git log --oneline
     ```

     ![alt text](image-18.png)

   - Crea una nueva rama `bugfix/rollback-feature` desde ese commit:

     ```bash
     $ git branch bugfix/rollback-feature <commit-hash>
     $ git checkout bugfix/rollback-feature
     ```

     ![alt text](image-1_1.png)

2. **Modificar y confirmar cambios en la nueva rama:**

   - Realiza algunas modificaciones en `main.py` que simulen una corrección de errores:

     ```python
     def greet():
         print('Fixed bug in feature')
     ```

   - Añade y confirma los cambios en la nueva rama:

     ```bash
     $ git add main.py
     $ git commit -m "Fix bug in rollback feature"
     ```

     ![alt text](image.png)

3. **Fusionar los cambios en la rama principal:**

   - Cambia de nuevo a la rama `main` y fusiona la rama `bugfix/rollback-feature`:

     ```bash
     $ git checkout main
     $ git merge bugfix/rollback-feature
     ```

     ![alt text](image-1.png)

4. **Explorar el historial después de la fusión:**

   - Usa `git log` y `git log --graph` para ver cómo se ha integrado el commit en el historial:

     ```bash
     $ git log --graph --oneline
     ```

     ![alt text](image-2.png)

5. **Eliminar la rama bugfix/rollback-feature:**

   - Una vez fusionados los cambios, elimina la rama `bugfix/rollback-feature`:

     ```bash
     $ git branch -d bugfix/rollback-feature
     ```

     ![alt text](image-19.png)

**Se utilizará una copia del repositorio para los siguientes ejercicios con el fin de evitar comprometer el principal**

Copia del repositorio [https://github.com/Janiopi/Actividades-CC3S2]

#### Ejercicio 4: Manipulación y restauración de commits con git reset y git restore

**Objetivo:** Comprender cómo usar `git reset` y `git restore` para deshacer cambios en el historial y en el área de trabajo.

**Instrucciones:**

1. **Hacer cambios en el archivo main.py:**

   - Edita el archivo `main.py` para introducir un nuevo cambio:
     ```python
     print('This change will be reset')
     ```
     ![alt text](image-20.png)
   - Añade y confirma los cambios:

     ```bash
     $ git add main.py
     $ git commit -m "Introduce a change to be reset"
     ```

     ![alt text](image-21.png)

2. **Usar git reset para deshacer el commit:**

   - Deshaz el commit utilizando `git reset` para volver al estado anterior:

     ```bash
     $ git reset --hard HEAD~1
     ```

     ![alt text](image-22.png)

   - Verifica que el commit ha sido eliminado del historial y que el archivo ha vuelto a su estado anterior.

   ![alt text](image-23.png)

3. **Usar git restore para deshacer cambios no confirmados:**

   - Realiza un cambio en `README.md` y no lo confirmes:

     ```bash
     $ echo "Another line in README" >> README.md
     $ git status
     ```

   - Usa `git restore` para deshacer este cambio no confirmado:

     ```bash
     $ git restore README.md
     ```

     ![alt text](image-24.png)

   - Verifica que el cambio no confirmado ha sido revertido.

   ![alt text](image-25.png)

#### Ejercicio 5: Trabajo colaborativo y manejo de Pull Requests

**Objetivo:** Simular un flujo de trabajo colaborativo utilizando ramas y pull requests.

**Instrucciones:**

1.  **Crear un nuevo repositorio remoto:**

    - Usa GitHub o GitLab para crear un nuevo repositorio remoto y clónalo localmente:

      ```bash
      $ git clone <URL-del-repositorio>
      ```

2.  **Crear una nueva rama para desarrollo de una característica:**

    - En tu repositorio local, crea una nueva rama `feature/team-feature`:

           ```bash
           $ git branch feature/team-feature
           $ git checkout feature/team-feature
           ```

      ![alt text](image-26.png)

3.  **Realizar cambios y enviar la rama al repositorio remoto:**

    - Realiza cambios en los archivos del proyecto y confírmalos:

      ```bash
      $ echo "print('Collaboration is key!')" > collaboration.py
      $ git add .
      $ git commit -m "Add collaboration script"
      ```

    - Envía la rama al repositorio remoto:

      ```bash
      $ git push origin feature/team-feature
      ```

      ![alt text](image-27.png)

4.  **Abrir un Pull Request:**

    - Abre un Pull Request (PR) en la plataforma remota (GitHub/GitLab) para fusionar `feature/team-feature` con la rama `main`.
    - Añade una descripción detallada del PR, explicando los cambios realizados y su propósito.

    ![alt text](image-28.png)

5.  **Revisar y fusionar el Pull Request:**

    - Simula la revisión de código, comenta en el PR y realiza cualquier cambio necesario basado en la retroalimentación.

    ![alt text](image-29.png)

    - Una vez aprobado, fusiona el PR en la rama `main`.
      ![alt text](image-30.png)

6.  **Eliminar la rama remota y local:**

    - Después de la fusión, elimina la rama tanto local como remotamente:

      ```bash
      $ git branch -d feature/team-feature
      $ git push origin --delete feature/team-feature
      ```

      ![alt text](image-31.png)

#### Ejercicio 6: Cherry-Picking y Git Stash

**Objetivo:** Aprender a aplicar commits específicos a otra rama utilizando `git cherry-pick` y a guardar temporalmente cambios no confirmados utilizando `git stash`.

**Instrucciones:**

1. **Hacer cambios en main.py y confirmarlos:**

   - Realiza y confirma varios cambios en `main.py` en la rama `main`:

     ```bash
     $ echo "print('Cherry pick this!')" >> main.py
     $ git add main.py
     $ git commit -m "Add cherry-pick example"
     ```

     ![alt text](image-32.png)

2. **Crear una nueva rama y aplicar el commit específico:**

   - Crea una nueva rama `feature/cherry-pick` y aplícale el commit específico:

     ```bash
     $ git branch feature/cherry-pick
     $ git checkout feature/cherry-pick
     $ git cherry-pick <commit-hash>
     ```

     ![alt text](image-33.png)

   ![ ](image-34.png)

3. **Guardar temporalmente cambios no confirmados:**

   - Realiza algunos cambios en `main.py` pero no los confirmes:

     ```bash
     $ echo "This change is stashed" >> main.py
     $ git status
     ```

     ![alt text](image-35.png)

   - Guarda temporalmente estos cambios utilizando `git stash`:

     ```bash
     $ git stash
     ```

     ![alt text](image-36.png)

4. **Aplicar los cambios guardados:**

   - Realiza otros cambios y confírmalos si es necesario.
   - Luego, recupera los cambios guardados anteriormente:

     ```bash
     $ git stash pop
     ```

     ![alt text](image-37.png)

5. **Revisar el historial y confirmar la correcta aplicación de los cambios:**

   - Usa `git log` para revisar el historial de commits y verificar que todos los cambios se han aplicado correctamente.

   ![alt text](image-38.png)
