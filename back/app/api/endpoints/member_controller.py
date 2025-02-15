import shutil
import os
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
from fastapi_restful.cbv import cbv


from app.common.repository.member_repository import MemberRepository
from app.common.dto.member_dto import MemberDTO, MemberAddDTO, MemberUpdateDTO


router = APIRouter()


@cbv(router)
class MemberAPI:

    @router.get("/all")
    async def get_all(self) -> list[MemberDTO]:
        result = await MemberRepository.get_all()
        return result

    @router.get("/{instance_id}")
    async def get_by_id(self, instance_id: int) -> MemberDTO:
        result = await MemberRepository.get_by_id(instance_id=instance_id)
        return result

    @router.post("/")
    async def add_member(self, data: MemberAddDTO) -> MemberDTO:
        converted_data = data.to_dict()
        result = await MemberRepository.add(**converted_data)
        return result

    @router.post("/upload/image")
    async def upload_member_image(self, image: UploadFile = File(...)):
        with open(f"app/static/images/member/{image.filename}.webp", "wb+") as file:
            shutil.copyfileobj(image.file, file)

    @router.get("/get/image")
    async def get_member_image(self, uuid: str) -> FileResponse:
        image_path = Path(f"app/static/images/member/{uuid}.webp")
        return FileResponse(image_path, media_type="image/webp")

    @router.patch("/")
    async def update_member(self, data: MemberUpdateDTO):
        member = await MemberRepository.get_by_id(instance_id=data.id)

        if member.image_id and data.image_id and (member.image_id != data.image_id):
            image_path = Path(f"app/static/images/member/{member.image_id}.webp")
            try:
                os.remove(path=image_path)
            except FileNotFoundError:
                pass

        await MemberRepository.update(data=data.to_dict())
        return "UPDATED"

    @router.delete("/{instance_id}")
    async def delete_member(seld, instance_id: int):
        member = await MemberRepository.get_by_id(instance_id=instance_id)

        if member.image_id:
            image_path = Path(f"app/static/images/member/{member.image_id}.webp")
            try:
                os.remove(path=image_path)
            except FileNotFoundError:
                pass

        await MemberRepository.delete(instance_id=instance_id)
        return "DELETED"
