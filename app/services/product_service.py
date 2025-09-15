from sqlalchemy.orm import Session
from fastapi import Depends
from app.models.product import Product 
from app.schemas.product import ProductCreate, ProductUpdate, ProductSchema 
from app.db.session import get_db
from app.crud.product import ProductCRUD

class ProductService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.product_crud = ProductCRUD()

    def add_product(self, product: ProductCreate):  
        return self.product_crud.create(self.db, product)

    def get_product(self, product_id: int):
        return self.product_crud.get(self.db, product_id)
    
    def get_all_products(self, skip: int = 0, limit: int = 100): 
        return self.product_crud.get_all(self.db, skip, limit)

    def update_product(self, product_id: int, updated_product: ProductUpdate):
        return self.product_crud.update(self.db, product_id, updated_product)

    def delete_product(self, product_id: int):
        return self.product_crud.delete(self.db, product_id)