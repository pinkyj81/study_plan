"""데이터베이스에 color 컬럼 추가"""
from db_config import db, init_db
from flask import Flask
from sqlalchemy import text

app = Flask(__name__)
init_db(app)

with app.app_context():
    try:
        # color 컬럼 추가
        db.session.execute(text('ALTER TABLE dbo.study_plan ADD color NVARCHAR(20) NULL'))
        db.session.commit()
        print('✅ color 컬럼이 성공적으로 추가되었습니다!')
    except Exception as e:
        if 'already exists' in str(e) or 'Column names in each table must be unique' in str(e):
            print('⚠️ color 컬럼이 이미 존재합니다.')
        else:
            print(f'❌ 오류 발생: {e}')
            db.session.rollback()
