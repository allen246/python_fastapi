from fastapi import APIRouter, Depends, Response
from fastapi import FastAPI, File, UploadFile, status, HTTPException
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from fastapi.responses import StreamingResponse
import io
router = APIRouter()


@router.post("/upload/")
async def upload_image(name: str ,image: UploadFile, db: Session = Depends(get_db)):
    # Read the image file contents
    image_data = image.file.read()

    # Save the image data to the database
    db_image = models.Profile(filename=image.filename, data=image_data)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)

    return {"message": "Profile uploaded successfully"}


@router.get("/download/{image_id}", status_code=200)
async def download_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(models.Profile).filter(models.Profile.id == image_id).first()

    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    return StreamingResponse(io.BytesIO(image.data), media_type="image/jpeg")

