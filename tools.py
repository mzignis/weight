import datetime

from sqlalchemy import insert
from sqlalchemy.orm import Session
import pandas as pd

from db import engine, DateWeightTable


def insert_record(date: datetime.date, weight: float):
    with engine.connect() as conn:
        query = insert(DateWeightTable.__table__).values(
            date=date,
            weight=weight
        )
        conn.execute(query)
        conn.commit()


def get_records() -> pd.DataFrame:
    with Session(engine) as session:
        df = pd.DataFrame(session.query(DateWeightTable.__table__).all())
    return df


if __name__ == '__main__':
    pass
