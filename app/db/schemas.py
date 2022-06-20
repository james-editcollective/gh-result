from pydantic import BaseModel


class PNUBase(BaseModel):
    pnu: str


class PNUItem(PNUBase):
    program: str
    error_desc: dict | None
    result: dict | None
    is_error: bool = False
    is_fix: bool = False

    class Config:
        orm_mode = True
