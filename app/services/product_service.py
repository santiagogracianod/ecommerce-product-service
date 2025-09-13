from app.models.product import ProductSchema

class ProductService:
    def __init__(self):
        self.products = {}

    def add_product(self, product: ProductSchema):
        self.products[product.id] = product

    def get_product(self, product_id: int):
        return self.products.get(product_id)

    def update_product(self, product_id: int, updated_product: ProductSchema):
        if product_id in self.products:
            self.products[product_id] = updated_product
            return True
        return False

    def delete_product(self, product_id: int):
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False