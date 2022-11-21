
from sqlalchemy.orm import Session


from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_metrics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Metric).offset(skip).limit(limit).all()

def get_metrics_byuser(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Metric).filter(models.Metric.owner_id == owner_id).offset(skip).limit(limit).all()


def create_user_metric(db: Session, metric: schemas.MetricCreate, user_id: int):
    db_metric = models.Metric(**metric.dict(), owner_id=user_id)
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

def update_metric(db:Session, metric: schemas.MetricUpdate, metric_id: int):
    db_metric = db.get(models.Metric, metric_id)
    if not db_metric:
        raise HTTPException(status_code=404, detail="Hero not found")
    metric_data = metric.dict(exclude_unset=True)
    for key, value in metric_data.items():
        setattr(db_metric, key, value)
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db.query(models.Metric).filter(models.Metric.id == metric_id)

def delete_metric(db: Session, metric_id: int):
    u = db.get(models.Metric, metric_id)
    db.delete(u)
    db.commit()
    return db.query(models.Metric).all()