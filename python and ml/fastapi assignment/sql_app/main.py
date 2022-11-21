from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user




@app.post("/users/{user_id}/metrics/", response_model=schemas.Metric)
def create_metric_for_user(
    user_id: int, metric: schemas.MetricCreate, db: Session = Depends(get_db)
):
    return crud.create_user_metric(db=db, metric=metric, user_id=user_id)


@app.get("/metrics/", response_model=List[schemas.Metric])
def read_metrics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = crud.get_metrics(db, skip=skip, limit=limit)
    return metrics

@app.patch("/metrics/{metric_id}", response_model = List[schemas.MetricUpdate])
def upate_metric(metric_id : int ,metric : schemas.MetricUpdate,db: Session = Depends(get_db)):
    return crud.update_metric(db = db, metric = metric, metric_id = metric_id)

@app.get("/metrics/{owner_id}", response_model=List[schemas.Metric])
def read_metrics(owner_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = crud.get_metrics_byuser(db,owner_id=owner_id, skip=skip, limit=limit)
    return metrics

@app.delete("/metrics/{metric_id}", response_model=List[schemas.Metric])
def delete_metric(metric_id : int, db: Session = Depends(get_db)):
    return crud.delete_metric(db, metric_id)