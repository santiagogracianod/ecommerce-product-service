from fastapi import FastAPI
# ...código existente...
from app.api.routes.products import router as product_router
# ...código existente...

app = FastAPI()
app.include_router(product_router)