from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict
from fastapi_pagination import Page, Params


class AddressSchema(BaseModel):
    address: str


class InfoSchema(AddressSchema):
    bandwidth: Optional[int] = None
    energy: Optional[int] = None
    trx: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class RequestSchema(InfoSchema):
    id: UUID
    date_time: datetime
