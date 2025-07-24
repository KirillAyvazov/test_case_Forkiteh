from uuid import uuid4
from math import ceil

from tronpy import Tron
from tronpy.exceptions import ApiError
from tronpy.providers import HTTPProvider
from requests.exceptions import HTTPError
from sqlalchemy import select, func
from fastapi_pagination import Params, Page

from schemas.schema import AddressSchema, InfoSchema, RequestSchema
from exeptions.exceptions import NotFoundError, ExceedingNumberRequests
from database.db_connect import async_session
from database.model import InfoModel


class Repository:
    def __init__(self):
        self._client = Tron(provider=HTTPProvider('https://api.trongrid.io'))
        self._session = async_session

    async def get_request(self, params: Params) -> Page:
        offset = (params.page - 1) * params.size
        count_query = select(func.count()).select_from(InfoModel)
        query = select(InfoModel).offset(offset).limit(params.size)
        async with self._session() as session:
            total_count = await session.execute(count_query)
            total = total_count.scalar()

            result = await session.execute(query)
            result = result.scalars().all()
            items = [RequestSchema.model_validate(i_model) for i_model in result]

            pagination = Page(
                items=items,
                total=total,
                page=params.page,
                pages=ceil(total / params.size),
                size=params.size
            )
            return pagination

    async def get_info(self, address: AddressSchema) -> InfoSchema:
        try:
            account_info = self._client.get_account(address.address)
            if account_info is None:
                raise NotFoundError

            info_schema = InfoSchema(
                address=address.address,
                bandwidth=self._client.get_bandwidth(address.address),
                energy=account_info.get("account_resource", {}).get("energy_usage"),
                trx=account_info.get("balance")
            )

            await self._write_in_db(info_schema)

            return info_schema

        except HTTPError:
            pass

        except ApiError:
            pass

        info_schema = await self._get_info_by_address(address.address)

        await self._write_in_db(info_schema)

        if info_schema:
            return info_schema

        raise ExceedingNumberRequests

    async def _write_in_db(self, info: InfoSchema) -> None:
        try:
            info_model = InfoModel(
                **info.model_dump(),
                id=uuid4()
                )

            async with self._session() as session:
                session.add(info_model)
                await session.commit()

        except Exception as e:
            print(e)

    async def _get_info_by_address(self, address: str) -> InfoSchema:
        try:
            query = select(InfoModel).where(InfoModel.address == address).order_by(InfoModel.date_time.desc())

            async with self._session() as session:
                result = await session.execute(query)
                info_model = result.scalars().first()
                if info_model:
                    info_schema = InfoSchema.model_validate(info_model)
                    return info_schema

        except Exception as e:
            print(e)


repo = Repository()


def get_repo() -> Repository:
    return repo
