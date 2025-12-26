# models.py
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, UniqueConstraint, CheckConstraint, String, Integer, Date

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)

    plans: Mapped[list["StudyPlan"]] = relationship(back_populates="user", cascade="all, delete-orphan")

class StudyPlan(db.Model):
    __tablename__ = "study_plan"
    plan_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(String(100))
    subject: Mapped[str] = mapped_column(String(50))
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)

    user: Mapped["User"] = relationship(back_populates="plans")
    days: Mapped[list["StudyDay"]] = relationship(back_populates="plan", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint("end_date >= start_date", name="ck_plan_date"),
    )

class StudyDay(db.Model):
    __tablename__ = "study_day"
    day_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    plan_id: Mapped[int] = mapped_column(ForeignKey("study_plan.plan_id", ondelete="CASCADE"))
    date_: Mapped[date] = mapped_column("date", Date, nullable=False)
    # planned/done/partial/missed/none
    status: Mapped[str] = mapped_column(String(12), default="planned")

    plan: Mapped["StudyPlan"] = relationship(back_populates="days")

    __table_args__ = (
        UniqueConstraint("plan_id", "date", name="uq_plan_day"),
        CheckConstraint("status in ('planned','done','partial','missed','none')", name="ck_status"),
    )
