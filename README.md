# Actividad Gestion de datos IA: Gestión y Persistencia de Datos de IA

Este proyecto es un tutorial interactivo diseñado para enseñar cómo un programa de **Python** puede actuar como un puente de comunicación. La aplicación toma resultados complejos (métricas de Inteligencia Artificial como Exactitud, Precisión y Recall), los organiza en una estructura limpia y los "teletransporta" desde un entorno de desarrollo local hasta una base de datos segura en la nube. 

El objetivo principal es que los datos dejen de ser temporales y pasen a ser **persistentes**, permitiendo que la información esté disponible en la nube de forma permanente.

---


### 🛡️ Justificación Técnica de la Selección

Para cumplir con los estándares de un entorno de IA en la nube, se seleccionaron estas herramientas bajo los siguientes criterios técnicos:

| Herramienta | Criterio Clave | Justificación Técnica |
| :--- | :--- | :--- |
| **GitHub Codespaces** | **Entorno de Desarrollo** | Proporciona un IDE basado en la nube (VS Code) que garantiza que el código corra igual en cualquier PC, eliminando problemas de "en mi máquina no funciona". |
| **GitHub** | **Control de Versiones** | Permite el rastreo de cambios y la integración continua (CI/CD) directa con plataformas de despliegue como Render. |
| **Python / Pandas** | **Compatibilidad** | Es el estándar de la industria para IA. Pandas ofrece una flexibilidad total para transformar datos crudos en estructuras listas para bases de datos SQL. |
| **Supabase (PostgreSQL)** | **Integración Cloud** | Ofrece una base de datos relacional robusta con acceso inmediato vía URL, facilitando la persistencia de datos desde cualquier servidor remoto. |
| **Render** | **Escalabilidad** | Permite que la aplicación crezca en recursos según la demanda y automatiza el despliegue cada vez que se detecta un cambio en el repositorio. |

> **Nota de Replicabilidad:** Esta combinación permite que cualquier desarrollador pueda clonar el repositorio en una nube pública (como AWS o Azure) y el sistema seguirá funcionando con ajustes mínimos de configuración.

---

## ¿Cómo funciona este sistema?

Conectamos tres piezas clave que trabajan en equipo para lograr un flujo de datos automatizado:

1.  **Python (El Procesador):** Es el cerebro que genera los datos. No solo crea las métricas, sino que utiliza lógica para validar que la conexión a internet sea segura antes de realizar el envío.
2.  **Supabase (El Almacén Remoto):** Es una base de datos **PostgreSQL** hospedada en la nube. Imagínala como un Excel superpotente que vive en la red y que solo acepta datos si presentas la "llave" (credenciales) correcta.
3.  **Render (El Host de Despliegue):** Es la plataforma que permite que tu código viva en un servidor profesional. Gracias a la integración con GitHub, Render detecta cambios y ejecuta el programa automáticamente sin que tu PC esté encendida.

---

## Herramientas que integran el ecosistema

Para que esta "teletransportación" de datos ocurra, integramos las siguientes librerías:

* **`pandas` (Gestión de Datos):** La librería estándar de ciencia de datos. La usamos para transformar listas de números en **DataFrames** (tablas organizadas), facilitando su manipulación.
* **`python-dotenv` (Seguridad de Credenciales):** Actúa como un escudo de protección. Permite que el programa lea la dirección de la base de datos desde un archivo oculto `.env`, evitando que tus contraseñas queden visibles en el código público.
* **`psycopg2` (El Conector de Base de Datos):** Es el motor de comunicación. Traduce las órdenes de Python al lenguaje de las bases de datos (SQL), gestionando la apertura y el cierre de conexiones de forma segura.
* **Connection Pooling:** Una técnica aplicada (configurando el **Puerto 5432**) para asegurar que la conexión sea estable y compatible con los protocolos de red actuales.

---

## Paso a Paso: Cómo configurar este proyecto

### 1. Preparar las librerías
Para que tu computadora entienda estas herramientas, abre tu terminal e instala los paquetes necesarios:
```bash
pip install pandas psycopg2-binary python-dotenv
```

### 2. Configurar llave maestra (.env)
El archivo `.env` es el corazon de la seguridad. Sigue estos pasos:
1. Crea un archivo nuevo en la raiz del proyecto llamado '.env'.
2. Define la variable ''DB_URL con tu cadena de conexion de Supabase:
```env
DB_URL=postgresql://postgres.egissbwcaavbvsneluxr:[Password]@aws-0-us-west-2.pooler.supabase.com:5432/postgres
```
<img width="1406" height="197" alt="image" src="https://github.com/user-attachments/assets/61d314f7-ad38-431c-a6b0-f39ae0b9e4fe" />

### 3. Conexión con la nube (Supabase)
En el panel de supabase, debes tener una tabla lista para recibir los datos:
* Tabla: metricas_ia
* Columnas: `Metricas` (Texto) y `Valor` (Números).
<img width="492" height="274" alt="image" src="https://github.com/user-attachments/assets/8754c192-1a16-48f6-a23b-d5db17245935" />

### 4. Despliegue en Render
Para que el proyecto funcione de forma independiente:
1. Conecta tu repositorio de Github a `Render`.
2. En la confirutacion de Render (`Environment Variables`) agrega la clave `DB_URL` con tu direccion de base de datos.

### Como correr el programa
Una vez configurado todo, simplemente ejecuta el archivo principal:
```bash
python main.py
```
### 5. Salida esperada por consola
Una vez preparado todos los archivos anteriores , la salida esperada por consola al ejecutar el script es la siguiente:
<img width="1646" height="201" alt="image" src="https://github.com/user-attachments/assets/f5ef9d39-2fc2-4a79-b8b7-61be60afb576" />



