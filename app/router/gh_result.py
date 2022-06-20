from fastapi import APIRouter, Depends, Request, Body, HTTPException
from sqlalchemy.orm import Session
import json

from ..db import schemas, crud


router = APIRouter(
    prefix="/gh_result",
    tags=["gh_result"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/", response_model=list[schemas.PNUItem])
async def read_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = crud.get_results(db, skip, limit)
    return results


@router.post("/", response_model=schemas.PNUItem)
async def create_result(payload: dict = Body(...), db: Session = Depends(get_db)):
    pnu = str(payload.get("pnu"))
    program = payload.get("type")[0]
    error_desc = payload.get("ErrorDict").get("value", None)
    error_dict = None
    is_error = False
    if error_desc:
        error_dict = json.loads(error_desc)
        is_error = True
    result = payload.get("attributes").get("value", None)
    result_dict = None
    if result:
        result_dict = json.loads(result)
    pnu_item = schemas.PNUItem(
        pnu=pnu,
        program=program,
        error_desc=error_dict,
        result=result_dict,
        is_error=is_error,
    )
    return crud.create_result(db, pnu_item)


@router.get("/{pnu}", response_model=schemas.PNUItem)
async def result_by_pnu(pnu: str, db: Session = Depends(get_db)):
    db_pnu_item = crud.get_result_by_pnu(db, pnu)
    if db_pnu_item is None:
        raise HTTPException(status_code=404, detail=f"{pnu} not found")
    return db_pnu_item
