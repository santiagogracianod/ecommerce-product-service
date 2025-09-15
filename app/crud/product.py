from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate
from typing import List, Optional
import uuid

class ProductCRUD:
    def create(self, db: Session, product_data: ProductCreate) -> Product:
        db_product = Product(**product_data.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    
    def get(self, db: Session, product_id: uuid.UUID) -> Optional[Product]:
        return db.query(Product).filter(Product.id == product_id).first()
    
    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[Product]:
        return db.query(Product).offset(skip).limit(limit).all()
    
    def update(self, db: Session, product_id: uuid.UUID, product_data: ProductUpdate) -> Optional[Product]:
        db_product = self.get(db, product_id)
        if not db_product:
            return None
        
        update_data = product_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_product, key, value)
        
        db.commit()
        db.refresh(db_product)
        return db_product
    
    def delete(self, db: Session, product_id: uuid.UUID) -> bool:
        db_product = self.get(db, product_id)
        if not db_product:
            return False
        
        db.delete(db_product)  # Hard delete
        db.commit()
        return True