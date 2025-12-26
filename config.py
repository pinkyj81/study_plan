# config.py
import os

class Config:
    # 1) 기본: 로컬 즉시 실행 (SQLite)
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URL", "sqlite:///study_calendar.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False

    # 편의 옵션
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")


"""
[ MSSQL 연결 문자열 예시 ]
- SQL Server (ODBC Driver 18) 권장
- 비밀번호에 특수문자 포함 시 URL 인코딩 필요

1) 기본 신뢰(권장. 사내/사설 인증서인 경우):
DB_URL="mssql+pyodbc://USER:P%40ssw0rd@YOURSERVER,1433/YOURDB?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

2) Azure 등 공개 CA 인증서가 있고 검증 통과 가능한 경우:
DB_URL="mssql+pyodbc://USER:P%40ssw0rd@YOURSERVER,1433/YOURDB?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes"

※ Render 배포에서 'self-signed' 오류가 나오면 위 1)처럼
  TrustServerCertificate=yes 를 꼭 붙여주세요.
"""
