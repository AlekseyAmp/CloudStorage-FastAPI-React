from fastapi import APIRouter, Depends

from services import user_services as u_s


router = APIRouter()


@router.patch("/settings/email/{new_email}")
async def change_email(new_email: str, user_id: u_s.get_user_id = Depends()):
    return await u_s.change_email(user_id, new_email)