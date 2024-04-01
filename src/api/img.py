from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter()


@router.get("/images/{image_path}", tags=["images"])
async def get_images(image: str):
    return FileResponse(image)
