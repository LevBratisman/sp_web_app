from app.common.dto.base import BaseDTO, IdBase


class Member(BaseDTO):
    name: str
    role: str
    image_id: str
    class_year: str | None
    faculty: str | None
    major: str | None
    major_code: str | None


class MemberAddDTO(Member):
    pass


class MemberUpdateDTO(IdBase):
    name: str
    role: str
    image_id: str
    class_year: str | None
    faculty: str | None
    major: str | None
    major_code: str | None


class MemberDTO(Member, IdBase):
    pass