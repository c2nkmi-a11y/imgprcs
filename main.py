from fastapi import FastAPI
from app.api.routes import auth, images

app = FastAPI(title="Image Processing API", version="1.0")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(images.router, prefix="/images", tags=["images"])