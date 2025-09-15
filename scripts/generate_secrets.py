"""
Script para generar claves secretas seguras para el proyecto
Uso: python scripts/generate_secrets.py
"""
import secrets
import string
import sys
from pathlib import Path

def generate_secret_key(length: int = 32) -> str:
    """Genera una clave secreta segura usando URL-safe base64"""
    return secrets.token_urlsafe(length)

def generate_jwt_secret(length: int = 64) -> str:
    """Genera una clave específica para JWT tokens"""
    return secrets.token_urlsafe(length)

def generate_database_password(length: int = 16) -> str:
    """Genera una contraseña segura para base de datos"""
    # Caracteres seguros para contraseñas de DB (evita caracteres problemáticos)
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*+-="
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def generate_random_string(length: int = 12) -> str:
    """Genera una string aleatoria para nombres de usuario, etc."""
    alphabet = string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def generate_hex_token(length: int = 32) -> str:
    """Genera un token hexadecimal"""
    return secrets.token_hex(length)

def create_env_template():
    """Crea un template .env con valores seguros generados"""
    
    secret_key = generate_secret_key(64)
    jwt_secret = generate_jwt_secret(64)
    db_password = generate_database_password(20)
    db_user = f"app_user_{generate_random_string(8)}"
    db_name = f"app_db_{generate_random_string(6)}"
    
    template = f"""# Database Configuration
DATABASE_URL=postgresql://{db_user}:{db_password}@localhost:5432/{db_name}

# API Configuration
API_TITLE=Ecommerce Product Service
API_VERSION=1.0.0
ENVIRONMENT=production
DEBUG=False

# Security Configuration - GENERADO AUTOMÁTICAMENTE
SECRET_KEY={secret_key}
JWT_SECRET_KEY={jwt_secret}
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS and Security
ALLOWED_HOSTS=your-domain.com,api.your-domain.com
CORS_ORIGINS=https://your-frontend.com,https://admin.your-domain.com

# Additional Security
BCRYPT_ROUNDS=12
SESSION_TIMEOUT=3600
MAX_LOGIN_ATTEMPTS=5
"""
    
    return template, {
        'secret_key': secret_key,
        'jwt_secret': jwt_secret,
        'db_user': db_user,
        'db_password': db_password,
        'db_name': db_name
    }

def main():
    """Función principal del script"""
    print("🔐 GENERADOR DE SECRETOS SEGUROS")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "key":
            print(f"SECRET_KEY={generate_secret_key()}")
            
        elif command == "jwt":
            print(f"JWT_SECRET_KEY={generate_jwt_secret()}")
            
        elif command == "password":
            length = int(sys.argv[2]) if len(sys.argv) > 2 else 16
            print(f"PASSWORD={generate_database_password(length)}")
            
        elif command == "template":
            template, secrets_info = create_env_template()
            
            # Crear archivo .env.production
            env_file = Path("../.env.production")
            with open(env_file, "w") as f:
                f.write(template)
            
            print(f"✅ Archivo creado: {env_file}")
            print("\n📋 RESUMEN DE SECRETOS GENERADOS:")
            print("-" * 40)
            for key, value in secrets_info.items():
                print(f"{key}: {value}")
            
        elif command == "help":
            show_help()
            
        else:
            print(f"❌ Comando desconocido: {command}")
            show_help()
    else:
        # Modo interactivo
        interactive_mode()

def interactive_mode():
    """Modo interactivo para generar secretos"""
    print("\n🎯 MODO INTERACTIVO")
    print("Selecciona qué generar:")
    print("1. Clave secreta general")
    print("2. Clave JWT")
    print("3. Contraseña de base de datos")
    print("4. Template completo .env.production")
    print("5. Todos los secretos individuales")
    
    choice = input("\nElige una opción (1-5): ").strip()
    
    if choice == "1":
        print(f"\n🔑 SECRET_KEY={generate_secret_key()}")
        
    elif choice == "2":
        print(f"\n🎫 JWT_SECRET_KEY={generate_jwt_secret()}")
        
    elif choice == "3":
        length = input("Longitud de contraseña (16): ").strip()
        length = int(length) if length else 16
        print(f"\n🔒 DB_PASSWORD={generate_database_password(length)}")
        
    elif choice == "4":
        template, secrets_info = create_env_template()
        print("\n📄 TEMPLATE .env.production GENERADO:")
        print("-" * 50)
        print(template)
        
        save = input("\n¿Guardar en archivo? (y/N): ").strip().lower()
        if save == 'y':
            env_file = Path("../.env.production")
            with open(env_file, "w") as f:
                f.write(template)
            print(f"✅ Guardado en: {env_file}")
            
    elif choice == "5":
        print("\n🔐 TODOS LOS SECRETOS:")
        print("-" * 30)
        print(f"SECRET_KEY={generate_secret_key()}")
        print(f"JWT_SECRET_KEY={generate_jwt_secret()}")
        print(f"DB_PASSWORD={generate_database_password()}")
        print(f"RANDOM_TOKEN={generate_hex_token()}")
        print(f"API_KEY={generate_secret_key(48)}")
        
    else:
        print("❌ Opción inválida")

def show_help():
    """Muestra la ayuda del script"""
    print("""
📖 USO DEL SCRIPT:

Modo interactivo:
    python scripts/generate_secrets.py

Comandos específicos:
    python scripts/generate_secrets.py key          # Clave secreta
    python scripts/generate_secrets.py jwt          # Clave JWT
    python scripts/generate_secrets.py password [longitud]  # Contraseña DB
    python scripts/generate_secrets.py template     # Template .env completo
    python scripts/generate_secrets.py help         # Esta ayuda

Ejemplos:
    python scripts/generate_secrets.py password 20
    python scripts/generate_secrets.py template

⚠️  IMPORTANTE:
- Guarda estos secretos en un lugar seguro
- NO los commitees al repositorio
- Úsalos solo en producción
- Rota las claves regularmente
""")

if __name__ == "__main__":
    main()