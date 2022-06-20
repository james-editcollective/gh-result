from sqlalchemy.orm import Session

from . import models, schemas


def create_result(db: Session, pnu_item: schemas.PNUItem):
    db_pnu_item = models.PNUItem(
        pnu=pnu_item.pnu,
        program=pnu_item.program,
        error_desc=pnu_item.error_desc,
        result=pnu_item.result,
        is_error=pnu_item.is_error,
        is_fix=pnu_item.is_fix,
    )
    db.add(db_pnu_item)
    db.commit()
    db.refresh(db_pnu_item)
    return db_pnu_item


def update_result(db: Session, pnu_item: schemas.PNUItem):
    old_result = db.query(models.PNUItem).filter(models.PNUItem.pnu == pnu_item.pnu)
    if not old_result.first():
        return None

    old_result.update(
        {
            "pnu": pnu_item.pnu,
            "program": pnu_item.program,
            "error_desc": pnu_item.error_desc,
            "result": pnu_item.result,
            "is_error": pnu_item.is_error,
            "is_fix": pnu_item.is_fix,
        }
    )
    db.commit()
    return old_result.first()


def get_result_by_pnu(db: Session, pnu: int):
    return db.query(models.PNUItem).filter(models.PNUItem.pnu == pnu).first()


def get_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PNUItem).offset(skip).limit(limit).all()
