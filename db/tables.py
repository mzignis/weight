from sqlalchemy import Column, Date, Double, Integer, Table
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DateWeightTable(Base):
    __table__ = Table(
        "date_weight",
        Base.metadata,
        Column("id", Integer, primary_key=True),
        Column("date", Date),
        Column("weight", Double),
    )
