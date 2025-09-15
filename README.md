> 🚧 En desarrollo

# 🛒 Ecommerce Product Microservice

Microservicio para la gestión de productos en un sistema de e-commerce, desarrollado con [FastAPI](https://fastapi.tiangolo.com/).

![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-green)
![Python](https://img.shields.io/badge/Python-3.12.1-blue)
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-yellow)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

<!--![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)-->
<!--![Security](https://img.shields.io/badge/Security-OWASP%20Top%2010-brightgreen)-->
<!--![License]()-->
---

## 🚀 Características

- ✨ CRUD de productos (crear, leer, actualizar, eliminar)
- 📄 API RESTful con documentación automática (Swagger/OpenAPI)
- 🧩 Estructura modular y escalable
- 🐳 Listo para contenerización con Docker
- 🧪 Preparado para integración con bases de datos y pruebas unitarias *(En desarrollo)*

---

## 📁 Estructura del Proyecto

```text
/workspaces/ecommerce-product-service/
├── app/
│   ├── __init__.py
│   ├── main.py                          # Punto de entrada de la aplicación
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py                    # Configuración y variables de entorno
│   │   ├── security.py                  # Funciones de seguridad
│   │   └── exceptions.py                # Excepciones personalizadas
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py                      # Dependencias compartidas
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py                   # Router principal de la API
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           └── products.py          # Endpoints de productos
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── base.py                      # CRUD base genérico
│   │   └── product.py                   # CRUD específico de productos
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py                      # Base SQLAlchemy
│   │   ├── session.py                   # Configuración de sesión DB
│   │   └── init_db.py                   # Inicialización de DB
│   ├── models/
│   │   ├── __init__.py
│   │   └── product.py                   # Modelos SQLAlchemy
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── product.py                   # Schemas Pydantic (YA EXISTE)
│   ├── services/
│   │   ├── __init__.py
│   │   └── product_service.py           # Lógica de negocio
│   └── utils/
│       ├── __init__.py
│       └── helpers.py                   # Utilidades generales
├── tests/
│   ├── __init__.py
│   ├── conftest.py                      # Configuración de pytest
│   ├── api/
│   │   ├── __init__.py
│   │   └── test_products.py             # Tests de endpoints
│   ├── crud/
│   │   ├── __init__.py
│   │   └── test_product.py              # Tests de CRUD
│   └── services/
│       ├── __init__.py
│       └── test_product_service.py      # Tests de servicios
├── alembic/                             # Migraciones de base de datos
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── docs/                                # Documentación adicional
│   └── api.md
├── scripts/                             # Scripts de utilidad
│   ├── init_db.py
│   └── seed_data.py
├── .env                                 # Variables de entorno (local)
├── .env.example                         # Ejemplo de variables de entorno
├── .gitignore
├── alembic.ini                          # Configuración de Alembic
├── docker-compose.yml                   # Para desarrollo local
├── Dockerfile                           # Ya existe
├── pyproject.toml                       # Configuración de dependencias
├── requirements.txt                     # Ya existe
└── README.md                            # Ya existe
```

Para más informacion mirar la [Wiki](https://github.com/RickContreras/ecommerce-product-service/wiki)
---

## ⚙️ Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/RickContreras/ecommerce-product-service
   cd ecommerce-product-service
   ```

2. **Crea y activa un entorno virtual**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements-devI.txt
   ```

### 📦 Dependencias Python principales *(En desarrollo)*

- `fastapi`
- `uvicorn[standard]`
- `sqlalchemy`
- `psycopg2-binary`
- `pydantic`

P**Posibles librerías para futuro:**

- `black`, `isort`, `flake8`, `mypy` (calidad y estilo de código)
- `pytest`, `pytest-cov`, `httpx` (🧪 Testing y calidad de código)
- `python-dotenv` (entorno y configuración)
- `mkdocs`, `Sphinx` (documentación)
- `bandit` (seguridad)
- `alembic`, `databases` (Migraciones y Acceso async a DB)
- `orjson`, `python-multipart`, `loguru` (📦 Serialización, rendimiento y utilidades)
- `aiokafka`, `pika`, `faststream` (📡 Comunicación entre microservicios (si se usará eventos))

---

## 🔐 Configuración de Seguridad

**⚠️ IMPORTANTE**: Este proyecto NO incluye credenciales reales por seguridad.

### Primera configuración:

1. **Genera credenciales seguras:**
   ```bash
   python scripts/generate_secrets.py template
   ```

2. **Copia y personaliza tu configuración:**
   ```bash
   cp .env.example .env
   # Edita .env con tus credenciales reales
   ```

3. **Variables de entorno requeridas:**
   - `DATABASE_URL` - Conexión a PostgreSQL## 🔐 Configuración de Seguridad

**⚠️ IMPORTANTE**: Este proyecto NO incluye credenciales reales por seguridad.

### Primera configuración:

1. **Genera credenciales seguras:**
   ```bash
   python scripts/generate_secrets.py template
   ```

2. **Copia y personaliza tu configuración:**
   ```bash
   cp .env.example .env
   # Edita .env con tus credenciales reales
   ```

3. **Variables de entorno requeridas:**
   - `DATABASE_URL` - Conexión a PostgreSQL

## 🏃 Ejecución en desarrollo

```bash
uvicorn app.main:app --reload
```

Accede a la documentación interactiva en [http://localhost:8000/docs](http://localhost:8000/docs).

---

## 🐳 Docker

1. **Construye la imagen**
   ```bash
   docker build -t ecommerce-product-service .
   ```

2. **Ejecuta el contenedor**
   ```bash
   docker run -p 8000:8000 ecommerce-product-service
   ```

---

## 🧪 Pruebas *(En desarrollo)*

Ejecuta las pruebas unitarias con:

```bash
pytest
```

---

## 🧹 Formateo y calidad de código *(En desarrollo)*

Formatea y verifica la calidad del código con:

```bash
black .
isort .
flake8 .
```

---

## 📚 Endpoints principales

| Método | Endpoint                   | Descripción           |
|--------|----------------------------|-----------------------|
| POST   | `/products`                | Crear producto        |
| GET    | `/products/{product_id}`   | Obtener producto por ID|
| PUT    | `/products/{product_id}`   | Actualizar producto   |
| DELETE | `/products/{product_id}`   | Eliminar producto     |

---

## 📝 Requisitos

- **Python 3.12.1**
- **Docker** (opcional)
- **PostgreSQL** (opcional, para persistencia)
- **Linux, macOS o Windows**

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!  
Por favor, abre un issue o envía un pull request siguiendo las [buenas prácticas de Git y Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/).

---

> Desarrollado por [RickContreras](https://github.com/RickContreras)