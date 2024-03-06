from __future__ import annotations

from typing import Annotated

from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy.ext.declarative import ConcreteBase
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.orm import with_polymorphic
from sqlalchemy.ext.declarative import declarative_base
intpk = Annotated[int, mapped_column(primary_key=True)]
str50 = Annotated[str, mapped_column(String(50))]


class Base(DeclarativeBase):
    pass


class Company(Base):
    __tablename__ = "company"
    id: Mapped[intpk]
    name: Mapped[str50]

    employees: Mapped[list[Person]] = relationship(
        back_populates="company", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Company {self.name}"


class Person(ConcreteBase, Base):
    __tablename__ = "person"
    id: Mapped[intpk]
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"))
    name: Mapped[str50]

    company: Mapped[Company] = relationship(back_populates="employees")

    __mapper_args__ = {
        "polymorphic_identity": "person",
    }

    def __repr__(self):
        return f"Ordinary person {self.name}"


class Engineer(Person):
    __tablename__ = "engineer"

    id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"))
    name: Mapped[str50]
    status: Mapped[str50]
    engineer_name: Mapped[str50]
    primary_language: Mapped[str50]

    company: Mapped[Company] = relationship(back_populates="employees")

    __mapper_args__ = {"polymorphic_identity": "engineer", "concrete": True}


class Manager(Person):
    __tablename__ = "manager"

    id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"))
    name: Mapped[str50]
    status: Mapped[str50]
    manager_name: Mapped[str50]

    company: Mapped[Company] = relationship(back_populates="employees")

    __mapper_args__ = {"polymorphic_identity": "manager", "concrete": True}

    def __repr__(self):
        return (
            f"Manager {self.name}, status {self.status}, "
            f"manager_name {self.manager_name}"
        )


if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://root:123456@localhost/sandbox?charset=utf8mb4")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        stmt = select(Company).where(Company.id == 1)
        result = session.scalars(stmt).one()
        print(result.name)
        print(result.employees)