from fastapi import FastAPI, HTTPException, Request, UploadFile, APIRouter, Depends
from config.database import GridFSSettings
from auth.oauth2 import AuthJWT
import auth.utils

app = FastAPI()

router = APIRouter()

grid_fs = GridFSSettings()


@router.post("/uploadfile")
async def upload_file(file: UploadFile, request: Request, Authorize: AuthJWT = Depends()):
    user_id = await auth.utils.check_auth(request, Authorize)
    file_id = grid_fs.file.put(
        file.file,
        filename=file.filename,
        content_type=file.content_type,
        metadata={
            "user_id": user_id,
            "is_deleted": False,
            "is_favorite": False,
        }
    )
    return {"file_id": str(file_id)}
