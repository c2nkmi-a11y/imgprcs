from pydantic import BaseModel
from uuid import UUID

class ImageResponse(BaseModel):
    id: UUID
    user_id: UUID
    filename: str
    filepath: str
    processed_filepath: str | None
    width: int | None
    height: int | None
    format: str | None
    status: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True