from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Params, Page
from tronpy.exceptions import BadAddress

from exeptions.exceptions import NotFoundError, ExceedingNumberRequests
from repository.repo import get_repo, Repository
from schemas.schema import AddressSchema, InfoSchema

router = APIRouter(prefix="/address_info", tags=["tron"])


@router.get("/request", response_model=Page, status_code=200)
async def get_request(
    params: Params = Depends(),
    repo: Repository = Depends(get_repo),
) -> Page:
    """
        Эндпоинт для получения списка запросов с пагинацией
    """
    # try:
    return await repo.get_request(params)
    #except Exception:
    #    raise HTTPException(status_code=500, detail="Internal server error")


@router.post("", response_model=InfoSchema, status_code=200)
async def get_info(
    address: AddressSchema,
    repo: Repository = Depends(get_repo),
) -> InfoSchema:
    """Эндпоинт для получения информации по адресу"""
    try:
        return await repo.get_info(address)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Not Found Error")
    except BadAddress:
        raise HTTPException(status_code=400, detail="No Valid Addres")
    except ExceedingNumberRequests:
        raise HTTPException(status_code=400, detail="The allowed number of requests has been exceeded. Repeat later")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
