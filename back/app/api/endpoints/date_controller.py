import shutil
import os
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
from fastapi_restful.cbv import cbv


from app.common.repository.date_repository import DateRepository
from app.common.dto.date_dto import DateDTO, DateAddDTO, DateUpdateDTO


router = APIRouter()


@cbv(router)
class DateAPI:

    @router.get("/all")
    async def get_all(self) -> list[DateDTO]:
        result = await DateRepository.get_all()
        return result

    @router.get("/{instance_id}")
    async def get_by_id(self, instance_id: int) -> DateDTO:
        result = await DateRepository.get_by_id(instance_id=instance_id)
        return result

    @router.post("/")
    async def add_date(self, data: DateAddDTO) -> DateDTO:
        converted_data = data.to_dict()
        result = await DateRepository.add(**converted_data)
        return result

    @router.patch("/")
    async def update_date(self, data: DateUpdateDTO):
        await DateRepository.update(data=data.to_dict())
        return "UPDATED"

    @router.delete("/{instance_id}")
    async def delete_date(seld, instance_id: int):
        await DateRepository.delete(instance_id=instance_id)
        return "DELETED"
