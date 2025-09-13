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
ecommerce-product-service/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── products.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── session.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   ├── crud/
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── product_service.py
│   │
│   └── __init__.py
│
├── tests/
│   ├── __init__.py
│   └── test_products.py
│
├── .env
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
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
   pip install -r requirements.txt
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