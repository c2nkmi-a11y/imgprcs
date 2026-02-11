from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.utilis.file import read_image
from app.models.image import Image, ImageStats
from app.services.statistics import image_statistics

router = APIRouter()
"""This module defines the API routes for image processing, including uploading images and retrieving their statistics.
"""
@router.post("/upload")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    stats = image_statistics(contents)

    img = Image(
        filename=file.filename,
        width=stats.width,
        height=stats.height,
        content_type=file.content_type

    )

    # Here you would typically save the image and stats to a database
    db.add(img)
    db.commit()
    db.refresh(img)

    db_stats = ImageStats(
        image_id=img.id, **img.dict())
    db.add(db_stats)
    db.commit()


    """    This endpoint allows users to upload an image file. It reads the image, calculates its statistics, and saves both the image metadata and statistics to the database. The response includes the filename, dimensions, content type, and calculated statistics of the uploaded image."""
    return {
        "filename": file.filename,
        "width": img.shape[1],
        "height": img.shape[0],
        "content_type": file.content_type,
        "statistics": img.statistics
    }