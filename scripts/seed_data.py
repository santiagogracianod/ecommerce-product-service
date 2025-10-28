#!/usr/bin/env python3
"""
Script para poblar la base de datos con productos reales
"""
import sys
import os

# Agregar el directorio raíz al path para importar módulos de la app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.product import Product
from decimal import Decimal

def create_real_products():
    """Crear productos reales en la base de datos"""
    
    products_data = [
        {
            "name": "iPhone 15 Pro Max",
            "description": "El iPhone más avanzado con chip A17 Pro, cámara de 48MP con zoom óptico 5x, y titanio de grado aeroespacial. Incluye Dynamic Island y USB-C.",
            "price": Decimal("1199.99"),
            "image_url": "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=500&h=500&fit=crop",
            "category": "Smartphones",
            "stock": 25
        },
        {
            "name": "MacBook Pro 14\" M3",
            "description": "MacBook Pro de 14 pulgadas con chip M3, 8GB de memoria unificada, SSD de 512GB. Perfecto para profesionales creativos y desarrolladores.",
            "price": Decimal("1599.00"),
            "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&h=500&fit=crop",
            "category": "Laptops",
            "stock": 15
        },
        {
            "name": "AirPods Pro (3ª generación)",
            "description": "Audífonos inalámbricos con cancelación activa de ruido, audio espacial personalizado y hasta 6 horas de reproducción.",
            "price": Decimal("249.99"),
            "image_url": "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=500&h=500&fit=crop",
            "category": "Audio",
            "stock": 50
        },
        {
            "name": "Samsung Galaxy S24 Ultra",
            "description": "Smartphone premium con S Pen integrado, cámara de 200MP, pantalla Dynamic AMOLED de 6.8 pulgadas y batería de 5000mAh.",
            "price": Decimal("1299.99"),
            "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&h=500&fit=crop",
            "category": "Smartphones",
            "stock": 20
        },
        {
            "name": "Sony WH-1000XM5",
            "description": "Audífonos over-ear con la mejor cancelación de ruido del mercado, 30 horas de batería y calidad de sonido Hi-Res.",
            "price": Decimal("399.99"),
            "image_url": "https://images.unsplash.com/photo-1583394838336-acd977736f90?w=500&h=500&fit=crop",
            "category": "Audio",
            "stock": 30
        },
        {
            "name": "Dell XPS 13 Plus",
            "description": "Ultrabook premium con procesador Intel Core i7 de 12ª generación, 16GB RAM, SSD 1TB y pantalla InfinityEdge de 13.4 pulgadas.",
            "price": Decimal("1449.00"),
            "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500&h=500&fit=crop",
            "category": "Laptops",
            "stock": 12
        },
        {
            "name": "iPad Pro 12.9\" M2",
            "description": "iPad Pro con chip M2, pantalla Liquid Retina XDR de 12.9 pulgadas, compatible con Apple Pencil y Magic Keyboard.",
            "price": Decimal("1099.00"),
            "image_url": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500&h=500&fit=crop",
            "category": "Tablets",
            "stock": 18
        },
        {
            "name": "Nintendo Switch OLED",
            "description": "Consola híbrida con pantalla OLED de 7 pulgadas, 64GB de almacenamiento interno y dock mejorado con puerto LAN.",
            "price": Decimal("349.99"),
            "image_url": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=500&h=500&fit=crop",
            "category": "Gaming",
            "stock": 35
        },
        {
            "name": "Apple Watch Series 9",
            "description": "Smartwatch con chip S9, pantalla Always-On Retina, GPS, seguimiento de salud avanzado y resistencia al agua hasta 50 metros.",
            "price": Decimal("429.00"),
            "image_url": "https://images.unsplash.com/photo-1579586337278-3f436f25d4d3?w=500&h=500&fit=crop",
            "category": "Smartwatches",
            "stock": 40
        },
        {
            "name": "Canon EOS R6 Mark II",
            "description": "Cámara mirrorless full-frame con sensor de 24.2MP, grabación de video 4K 60p, estabilización de imagen de 8 pasos y enfoque automático dual pixel.",
            "price": Decimal("2499.00"),
            "image_url": "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500&h=500&fit=crop",
            "category": "Fotografía",
            "stock": 8
        }
    ]
    
    db = SessionLocal()
    try:
        # Eliminar productos existentes para empezar limpio
        db.query(Product).delete()
        db.commit()
        
        print("🗑️  Productos existentes eliminados")
        
        # Crear nuevos productos
        products_created = []
        for product_data in products_data:
            product = Product(**product_data)
            db.add(product)
            products_created.append(product_data["name"])
        
        db.commit()
        
        print(f"✅ {len(products_created)} productos creados exitosamente:")
        for i, name in enumerate(products_created, 1):
            print(f"   {i}. {name}")
        
        # Verificar que se crearon correctamente
        count = db.query(Product).count()
        print(f"\n📊 Total de productos en la base de datos: {count}")
        
    except Exception as e:
        print(f"❌ Error al crear productos: {e}")
        db.rollback()
    finally:
        db.close()

def main():
    """Función principal para poblar la base de datos"""
    print("🚀 Iniciando creación de productos reales...")
    create_real_products()
    print("🎉 ¡Proceso completado!")

if __name__ == "__main__":
    main()