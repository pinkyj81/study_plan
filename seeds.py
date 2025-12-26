# seed.py
from datetime import date
from app import create_app, db, User, StudyPlan

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    u = User(name="Demo", email="demo@user.com")
    db.session.add(u); db.session.commit()

    p1 = StudyPlan(user_id=u.user_id, title="TOEFL 단어 외우기", subject="TOEFL",
                   start_date=date(2025,1,1), end_date=date(2025,12,31))
    p2 = StudyPlan(user_id=u.user_id, title="Wordly wise 3000 #4", subject="영어 단어",
                   start_date=date(2025,10,1), end_date=date(2025,12,31))
    db.session.add_all([p1, p2]); db.session.commit()
    print("Seeded.")
