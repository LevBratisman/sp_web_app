import shutil
import os
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
from fastapi_restful.cbv import cbv


from app.common.repository.post_repository import PostRepository
from app.common.dto.post_dto import PostDTO, PostAddDTO, PostUpdateDTO


router = APIRouter()


@cbv(router)
class PostAPI:

    @router.get("/all")
    async def get_all(self) -> list[PostDTO]:
        result = await PostRepository.get_all()
        return result

    @router.get("/{instance_id}")
    async def get_by_id(self, instance_id: int) -> PostDTO:
        result = await PostRepository.get_by_id(instance_id=instance_id)
        return result

    @router.post("/")
    async def add_post(self, data: PostAddDTO) -> PostDTO:
        converted_data = data.to_dict()
        result = await PostRepository.add(**converted_data)
        return result

    @router.post("/upload/image")
    async def upload_post_image(self, image: UploadFile = File(...)):
        with open(f"app/static/images/post/{image.filename}.webp", "wb+") as file:
            shutil.copyfileobj(image.file, file)

    @router.get("/get/image")
    async def get_post_image(self, uuid: str) -> FileResponse:
        image_path = Path(f"app/static/images/post/{uuid}.webp")
        return FileResponse(image_path, media_type="image/webp")

    @router.patch("/")
    async def update_post(self, data: PostUpdateDTO):
        post = await PostRepository.get_by_id(instance_id=data.id)

        if post.image_id and data.image_id and (post.image_id != data.image_id):
            image_path = Path(f"app/static/images/post/{post.image_id}.webp")
            try:
                os.remove(path=image_path)
            except FileNotFoundError:
                pass

        await PostRepository.update(data=data.to_dict())
        return "UPDATED"

    @router.delete("/{instance_id}")
    async def delete_post(self, instance_id: int):
        post = await PostRepository.get_by_id(instance_id=instance_id)

        if post.image_id:
            image_path = Path(f"app/static/images/post/{post.image_id}.webp")
            try:
                os.remove(path=image_path)
            except FileNotFoundError:
                pass

        await PostRepository.delete(instance_id=instance_id)
        return "DELETED"

    @router.patch("/{instance_id}/like")
    async def like(self, instance_id: int):
        await PostRepository.like(instance_id=instance_id)

    @router.patch("/{instance_id}/dislike")
    async def dislike(self, instance_id: int):
        await PostRepository.dislike(instance_id=instance_id)
