from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate
from typing import List, Optional

class ProductCRUD:
    def create(self, db: Session, product_data: ProductCreate) -> Product:
        db_product = Product(**product_data.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    
    def get(self, db: Session, product_id: int) -> Optional[Product]:
        return db.query(Product).filter(Product.id == product_id, Product.is_active == True).first()
    
    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[Product]:
        return db.query(Product).filter(Product.is_active == True).offset(skip).limit(limit).all()
    
    def update(self, db: Session, product_id: int, product_data: ProductUpdate) -> Optional[Product]:
        db_product = self.get(db, product_id)
        if not db_product:
            return None
        
        update_data = product_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_product, key, value)
        
        db.commit()
        db.refresh(db_product)
        return db_product
    
    def delete(self, db: Session, product_id: int) -> bool:
        db_product = self.get(db, product_id)
        if not db_product:
            return False
        
        db_product.is_active = False  # Soft delete
        db.commit()
        return True