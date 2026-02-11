from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.image import ImageStats

router = APIRouter()

@router.get("/stats/{image_id}")
async def get_image_stats(image_id: str, db: Session = Depends(get_db)):
    stats = db.query(ImageStats).filter(ImageStats.image_id == image_id).first()
    if not stats:
        return {"error": "Statistics not found for the given image ID"}
    
    """This endpoint retrieves the statistics of a specific image based on its ID. It queries the database for the statistics associated with the provided image ID and returns them in a structured format. If no statistics are found, it returns an error message indicating that the statistics could not be found."""
    return {
        "image_id": stats.image_id,
        "mean_color": stats.mean_color,
        "median_color": stats.median_color,
        "mode_color": stats.mode_color,
        "created_at": stats.created_at
    }