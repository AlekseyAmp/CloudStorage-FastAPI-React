from fastapi import APIRouter, Depends, UploadFile

from api.users.user_services import get_user_id
from api.files.file_services import upload_file, download_file, get_all_files


router = APIRouter()


@router.post("/upload_file")
async def upload_file_endpoint(file: UploadFile, user_id: get_user_id = Depends()):
    return {"file_id": await upload_file(file, user_id)}


@router.get("/download_file/{file_id}")
async def download_file_endpoint(file_id: str, user_id: get_user_id = Depends()):
    return await download_file(file_id, user_id)


@router.get("/all_files")
async def get_all_files_endpoint(user_id: get_user_id = Depends()):
    return await get_all_files(user_id)
