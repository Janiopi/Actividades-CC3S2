### Actividad: **Migrando a Microservicios: Docker, Kubernetes y CI/CD**

#### Escenario general

Tu equipo está desarrollando dos microservicios en Python (Users y Orders) que forman el núcleo de una plataforma de pedidos en línea. Quieres:

* Asegurar builds reproducibles y rápidos.
* Desplegar en un entorno local para pruebas de integración continua (CI).
* Evolucionar a un clúster de Kubernetes administrado en producción.
* Automatizar tests, builds y despliegues con GitHub Actions.

>Utiliza como referencia el siguiente repositorio: [Microservicios, Kubernetes y Github Actions](https://github.com/kapumota/DS/tree/main/2025-1/microservices-k8s)

#### A. Docker y Docker Compose

**Contexto:** Al empaquetar tus servicios, debe primar la consistencia entre entornos (dev, staging, prod) y minimizar el tiempo de despliegue.

1. **Arquitectura de contenedores**

   * Explica cómo un contenedor encapsula la aplicación y sus dependencias. ¿Qué ventajas ofrece frente a una VM en términos de arranque, consumo de recursos y portabilidad?

    - Un contenedor encapsula una aplicación mediante el uso de namespaces y cgroups del kernel de Linux
        - Namespace: Aislan procesos, red, sistema de archivos y usuarios
        - Cgroups: Limitan y controlan recursos (CPU, memoria)
        - Union File System: Crea capas inmutables que se combinan para formar el sistema de archivos del contenedor

    
    Consideraciones adicionales:
    
        - Volúmenes: Para un almacenamiento persistente de datos, se utilizan los volúmenes de Docker, que son áreas de almacenamiento separadas que no están sujetas a las limitaciones del sistema de archivos en capas del contenedor. 
        - Dockerfile: El Dockerfile es un archivo de texto que contiene las instrucciones para construir una imagen de Docker. 
        - Controladores de almacenamiento: Docker utiliza diferentes controladores de almacenamiento, como OverlayFS o Btrfs, para administrar el sistema de archivos en capas. 


    - Ventajas sobre VMs
        - Arranque: Segundos vs minutos (Contenedores más rapido,sin boot de SO completo)
        - Recursos: Comparten kernel de host(menor overhead)
        - Portabilidad: Funciona en mi máquina -> Funciona en cualquier lugar

   * En tu proyecto, ¿qué pasos ocurren al ejecutar `docker build -t user-service .` y por qué cada uno es crítico para garantizar una imagen fiable?

    - Lectura del DockerFile: Interpreta las instrucciones secuencialmente
    - Descarga de imagen base: Pull de imagen FROM de DockerHUb si no existe localmente
    - Creación de capas: Cada instrucción crea una nueva capa inmutable
    - Ejecución de comandos: RUN,COPY, ADD se ejecutan en contenedores temporales
    - Commit de capas: Cada capa se guarda en el cache local
    - Etiquetado: Se asinga el tag "user-service" a la imagen final





2. **Optimización de Dockerfile**

   * Analiza el `Dockerfile` de `service-user` y(diagrama de capas) justifica el orden de instrucciones.

   ![alt text](image-1.png)
   
Este es un Dockerfile estándar (no multi-etapa) para un servicio Python 

## Instrucciones y su propósito

```dockerfile
FROM python:3.10-slim
```
- Utiliza la imagen base `python:3.10-slim`, que proporciona Python 3.10 en una distribución Debian mínima
- Esta imagen base es ligera pero contiene lo necesario para ejecutar aplicaciones Python

```dockerfile
WORKDIR /app
```
- Establece el directorio de trabajo dentro del contenedor como `/app`
- Todas las instrucciones siguientes se ejecutarán en este contexto

```dockerfile
COPY requirements.txt .
```
- Copia el archivo de requisitos desde el host al contenedor
- Sólo copia este archivo específico, no todo el código fuente

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```
- Instala las dependencias Python definidas en requirements.txt
- `--no-cache-dir` evita almacenar archivos de caché de pip, reduciendo el tamaño de la imagen

```dockerfile
COPY app.py .
```
- Copia el archivo principal de la aplicación al contenedor

```dockerfile
EXPOSE 8000
```
- Documenta que el contenedor escucha en el puerto 8000
- No abre realmente el puerto, solo es informativo

```dockerfile
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```
- Define el comando que se ejecutará cuando el contenedor inicie
- Utiliza Uvicorn (un servidor ASGI) para ejecutar la aplicación FastAPI

## Justificación del orden

El orden de las instrucciones es crucial para optimizar el proceso de construcción de Docker y aprovechar su sistema de capas:

- **Capas más estables primero**: Docker almacena cada instrucción como una capa que puede ser reutilizada. Las capas que cambian menos frecuentemente se colocan primero.

- **Dependencias antes que código**: Al copiar y instalar las dependencias antes de copiar el código de la aplicación, Docker puede reutilizar estas capas cuando solo cambia el código fuente.

- **Minimizar reconstrucciones**: Si solo `app.py` cambia, solo se reejecutarán las últimas instrucciones del Dockerfile, ahorrando tiempo en el proceso de construcción.

- **Seguridad de las capas**: Este enfoque garantiza que las dependencias se instalen de manera reproducible, separadas de los cambios en el código.





   

# Propón optimizaciones (por ejemplo, combinar instrucciones RUN, usar imágenes base más ligeras) y detalla cómo mejorarían el tiempo de build o el tamaño de imagen.


   ![alt text](image.png)


**Optimizaciones propuestas:** 
- Multi-stage build: Reduce tamaño final
- Imagen base slim: Menos vulnerabilidades
- Copia de requirements.txt primero: Mejor cache de layers
- --no-cache-dir: Evita cache de pip


3. **Redes y volúmenes en un entorno real**

   * Si tu microservicio necesitara persistir sesiones o logs de auditoría, ¿cómo montarías un volumen Docker?
   ```
    # docker-compose.yml
    volumes:
    - ./logs:/app/logs
    - session-data:/app/sessions

    volumes:
    session-data:
        driver: local
   ```
   
   * En producción, ¿qué tipo de red usarías para comunicar los servicios `user` y `order` si estuviesen en distintos hosts, y por qué?

    ```
    # Red overlay para Docker Swarm
    docker network create --driver overlay --attachable microservices-net
    ```

    **Overlay Network**: Utilizado para crear conección entre Swarm services, también utilizado para conectar contenedores corriendo en diferentes hosts.
    **Swarm Services**: Componentes de aplicación que trabajan en conjunto para crear una app completa.  



4. **Docker Compose para entornos de desarrollo**

   * Diseña un `docker-compose.yml` que arranque:
     * `service-user` y `service-order`.
     * Una base de datos Redis para gestionar caché de sesión.
     * Un contenedor de administración (por ejemplo, phpMyAdmin o RedisInsight).
  
    ```
    version: '3.8'
    services:
        user-service:
            build: ./service-user
            ports:
                - "5001:5000"
            environment:
                - REDIS_URL=redis://redis:6379
            depends_on:
                - redis
            networks:
                - microservices
        
        order-service:
            build: ./service-order
            ports:
                - "5002:5000"
            environment:
                - REDIS_URL=redis://redis:6379
                - USER_SERVICE_URL=http://user-service:5000
            depends_on:
                - redis
                - user-service
            networks:
                - microservices
        
        redis:
            image: redis:7-alpine 
            ports:
                - "6379:6379"
            volumes: 
                - redis-data:/data
            networks:
                - microservices
        
        redis-insight:
            image: redislabs/redisinsight:latest
            ports:
                - "8001:8001"
            depends_on:
                - redis
            networks:
                - microservices
        
    volumes:
        redis-data:
    
    networks:
        microservices:
            driver: bridge

    ```
    Probando el docker-compose

    - `docker compose build`
    ![alt text](image-2.png)

    - `docker compose up`
    ![alt text](image-3.png)

* Explica cómo Compose acelera el onboarding de nuevos desarrolladores y facilita simular entornos de staging locales.
    - **Onboarding rápido**: Un comando `docker compose up` levanta todo
    - **Entorno idéntico**: Mismas versiones para todos
    - **Simulación de staging**: Comunicación entre servicios reales


#### B. Infraestructura como Código (IaC)

**Contexto:** En tu pipeline CI/CD quieres tratar los manifiestos de Kubernetes igual que el código: revisión por pull request, versionado, validación automática.

5. **Principios de IaC**

   * Define IaC y enumera sus tres beneficios principales (reproducibilidad, trazabilidad, rollback).

    - IaC (Inraestructure as Code) es la práctica de gestionar infraestrucutra mediante código declarativo, versionado y automatizado.
        - **Reproducibilidad**: Capacidad de crear la misma infraestructura en cualquier entorno
        - **Trazabilidad**: Historial completo de cambios (logs por ejemplo)
        - **Rollback**: Vuelta atrás rápida ante problemas (Algo parecido a un checkpoint)

   * Compara un script Bash que ejecute `kubectl apply` (imperativo) con un manifiesto YAML que describa un Deployment (declarativo). ¿Qué control de versiones y auditoría permite cada enfoque?
    
    
    - Imperativo
    ```
        kubectl create deployment user-service --image=user-service:latest
        kubectl scale deployment user-service --replicas=3
        kubectl expose deployment user-service --port=80
    ```

    - Declarativo
    ```
        apiVersion: apps/v1
        metadata:
            name: user-service
        spec:
            replicas:3
            selector:
                matchLabels:
                    app: user-service
            template:
             metadata:
                labels:
                    app: user-service
            spec:
                containers:
                - name: user-service
                  image: user-service:latest
                  ports: 
                  - containerPort: 5000
                        
    ```

6. **Manifiestos Kubernetes como código fuente**

   * En el directorio `k8s/`, identifica en cada YAML:

     * El tipo de objeto (`Deployment`, `Service`) y su propósito.
        La separación en Deployment y Service sigue la idea de "separación de responsabilidades"
        
        - **Deployment**:  Gestión del ciclo de vida de los Pods.
            - *Definición de aplicación*: Especifica qué contenedores ejecutar, qué imagen usar y cómo configurarlos
            - *Estado deseado*: Mantiene el número especificado de réplicas
            - *Actualizaciones progresivas*: Rolling updates
            - *Autorecuperación*: Si un pod falla, el deployment crea uno nuevo automáticamente
            - *Escalabilidad*: Permite aumentar o disminuir el número de réplicas fácilmente
            - *Historial de revisiones*: Mantiene un historial de despliegues para posibles rollbacks
        -**Service**: Abstracción de red y descubrimiento de servicios
            - *IP estable*: Proporciona una única dirección IP estable para acceder a los Pods
            - *Balanceo de carga*: Distribuye las solicitudes entre todos los pods del Deployment
            - *Descubrimiento de servicios*: Permite a otros componentes encontrar y comunicarse con este servicio mediante un nombre DNS estable.
            - *Abstracción*: Oculta detalles de implementación (como el número y ubicación de los pods)
            - *Continuidad de servicio*: Sigue funcionando aunque los pods individuales sean reemplazados o reubicados


   * ¿Cómo encajarías estos archivos en tu flujo de GitFlow para asegurar revisiones de infraestructura antes de merge?
        - **Feature branch**: Cambios en manifiestos
        - **Pull request**: Revisión de infraestructura
        - **Staging**: Aplicación automática tras merge
        - **Production**: Despliegue manual o automático


7. **Parametrización y reutilización**

   * Diseña un `ConfigMap` o `Secret` para extraer la URL de una base de datos PostgreSQL, de modo que puedas reutilizar el mismo Deployment en staging y producción cambiando sólo valores.
    ```
    # configmap.yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
        name: app-config
    data:
        DATABASE_URL: "postgresql://user:pass@postgres:5432/db"
        ENVIRONMENT: "development"
    ```

    ```
    # secret.yaml
    apiVersion: v1
    kind: Secret
    metadata:
        name: db-credentials
    type: Opaque
    data:
        username: dXNlcg==  # user (base64)
        password: cGFzcw==  # pass (base64)

    
    ```



   * Explica brevemente cómo Helm o Kustomize automatizarían la generación de estos manifiestos según variables de entorno o valores por entorno.


#### C. Fundamentos de Kubernetes

**Contexto:** En producción, la plataforma correrá en un clúster gestionado que debe escalar automáticamente y recuperarse de fallos.

8. **¿Por qué Kubernetes?**

   * Imagina que aumentas el tráfico en un 10× durante una campaña de Black Friday. ¿Cómo ayudaría Kubernetes frente a un orquestador casero hecho con scripts?
   * Compara rápidamente Kubernetes con Docker Swarm en cuanto a ecosistema, escalabilidad y extensibilidad.

9. **Modelado de la arquitectura**

   * Dibujarás un diagrama con al menos un nodo (VM), varias réplicas de Pods y dentro de cada Pod dos containers (uno de aplicación y otro sidecar de logging).
   * Explica cómo las probes (liveness/readiness) garantizan que el tráfico no llegue a Pods no preparados o con problemas.

10. **Estrategias de despliegue**

    * Describe el objeto `Deployment`, su historia de revisiones (`RevisionHistoryLimit`) y las estrategias de rollout (`RollingUpdate` vs `Recreate`).
    * Explica cuándo usar `ClusterIP`, `NodePort` o `LoadBalancer` para exponer cada uno de tus servicios y su impacto en entornos on-premise vs nube pública.


#### D. Kubernetes – Entorno local con Minikube

**Contexto:** Antes de integrar con el clúster real, tu pipeline de CI debe validar despliegues en un entorno local idéntico (lo más posible) al de producción.

11. **Instalación del CLI**

    * Detalla los pasos para instalar `kubectl` en tu SO preferido y cómo configurar el autocompletado.
    * Comenta los comandos `kubectl version`, `kubectl config view` y qué información esencial devuelven.

12. **Arranque de Minikube**

    * Explica qué sucede al lanzar `minikube start --driver=docker`: creación de VM, adaptación de red, instalación de kube-apiserver.
    * Compara Minikube con Kind en cuanto a facilidad de integración en CI y recursos requeridos.

13. **Script de despliegue local**

    * Desglosa el script `minikube-setup.sh` en secciones: inicialización, build de imágenes, despliegue de manifests.
    * ¿Qué ventajas y limitaciones tiene esta aproximación para pruebas de integración automática en GitHub Actions?

14. **Limpieza y recuperación**

    * Indica cómo listar y eliminar los recursos de Kubernetes creados (`kubectl get all`, `kubectl delete namespace`).
    * En caso de fallo de un Deployment, ¿qué pasos seguirías para recuperar el servicio sin downtime?


#### E. CI/CD con GitHub Actions

**Contexto:** El objetivo es lograr una pipeline end-to-end que valide código, construya imágenes y despliegue a Minikube (y más adelante a producción) sin intervención manual.

15. **Anatomía del workflow**

    * Describe cada sección de `.github/workflows/ci-cd.yaml`: disparadores (`on`), jobs, steps y acciones usadas.
    * ¿Cómo encajarías una etapa adicional de tests unitarios y de integración antes de la etapa de build?

16. **Acciones Docker y kubectl**

    * ¿Por qué se emplea `docker/setup-buildx-action`? Explica qué es Buildx.
    * En el contexto de un runner de Actions, ¿por qué `push: false` y cómo modificas el workflow para empujar imágenes a Docker Hub o un registry corporativo?

17. **Despliegue remoto**

    * Si migras a EKS/GKE en AWS/GCP, ¿qué credenciales y pasos cambiarían en tu workflow para autenticar `kubectl` y proteger secretos?
    * Propón una estrategia para usar `environments` de GitHub y aprobar despliegues a staging/producción manualmente.

#### F. Preparación para producción

**Contexto:** Tras validar todo localmente y en staging, debes diseñar cómo llevarlo a tu clúster de producción con seguridad, observabilidad y cero downtime.

18. **Canary y Blue-Green**

    * Diseña un manifiesto o describirías el proceso (usando herramientas como Argo Rollouts) para hacer un despliegue canary de tu `user-service`.

19. **Seguridad en contenedores**

    * Menciona tres buenas prácticas: escanear imágenes (Clair, Trivy), mínima base (`distroless`, **scratch**), políticas de PSP/OPA Gatekeeper.

20. **Monitoreo y logs**

    * Propón un stack basado en Prometheus, Grafana y ELK/EFK para métricas y logs de tus microservicios. Explica cómo integrar un sidecar de Fluentd o Filebeat.
