from fastapi import APIRouter, HTTPException
from src.models.product import ProductSchema
from src.services.product_service import ProductService

router = APIRouter()
product_service = ProductService()

@router.post("/products", response_model=ProductSchema, status_code=201)
def create_product(product: ProductSchema):
    product_service.add_product(product)
    return product

@router.get("/products/{product_id}", response_model=ProductSchema)
def get_product(product_id: int):
    prod = product_service.get_product(product_id)
    if prod:
        return prod
    raise HTTPException(status_code=404, detail="Product not found")

@router.put("/products/{product_id}", response_model=ProductSchema)
def update_product(product_id: int, product: ProductSchema):
    updated = product_service.update_product(product_id, product)
    if updated:
        return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    success = product_service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")