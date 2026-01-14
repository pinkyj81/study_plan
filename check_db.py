from app import app, db
from sqlalchemy import text

with app.app_context():
    result = db.session.execute(text('SELECT plan_id, title, image_url, color FROM dbo.study_plan')).fetchall()
    print('\n=== study_plan 테이블 데이터 ===')
    for r in result:
        img = r.image_url[:50] + '...' if r.image_url and len(r.image_url) > 50 else (r.image_url or 'NULL')
        print(f'plan_id: {r.plan_id}')
        print(f'  title: {r.title}')
        print(f'  image_url: {img}')
        print(f'  color: {r.color}')
        print()
