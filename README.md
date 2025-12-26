# 자기주도 학습 캘린더 📚

Flask 기반의 학습 계획 관리 및 진도 추적 웹 애플리케이션입니다.

## 주요 기능 ✨

- 📅 **연간 학습 캘린더**: 12개월 달력으로 학습 진도 한눈에 확인
- 📝 **학습 계획 관리**: 여러 학습 계획을 생성하고 관리
- 🎨 **계획별 색상 구분**: 각 계획을 다른 색상으로 시각화
- ✅ **진도 체크**: 학습 완료, 부분 완료, 미완료 상태 관리
- 📋 **템플릿 시스템**: 학습 내용을 템플릿으로 저장하고 재사용
- 👤 **사용자 인증**: 로그인/로그아웃 기능

## 기술 스택 🛠️

- **Backend**: Flask, SQLAlchemy
- **Database**: MS SQL Server
- **Frontend**: Tailwind CSS, Vanilla JavaScript
- **Python**: 3.14+

## 설치 방법 💻

1. 저장소 클론
```bash
git clone https://github.com/pinkyj81/study_plan.git
cd study_plan
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

4. 데이터베이스 설정
- `db_config.py`에서 데이터베이스 연결 정보 수정
- `create_tables.py` 실행하여 테이블 생성

5. 애플리케이션 실행
```bash
python app.py
```

6. 브라우저에서 접속
```
http://localhost:5000
```

## 프로젝트 구조 📁

```
study_calendar/
├── app.py              # 메인 애플리케이션
├── db_config.py        # 데이터베이스 설정
├── models.py           # 데이터 모델
├── create_tables.py    # 테이블 생성 스크립트
├── seeds.py            # 샘플 데이터
├── requirements.txt    # 패키지 의존성
├── static/             # 정적 파일 (CSS, JS, 이미지)
└── templates/          # HTML 템플릿
    ├── index.html          # 메인 캘린더 페이지
    ├── login.html          # 로그인 페이지
    └── template_manage.html # 템플릿 관리 페이지
```

## 사용 방법 📖

1. **로그인**: 사용자 이름으로 로그인 (자동 계정 생성)
2. **계획 생성**: "새 계획" 버튼으로 학습 계획 추가
3. **날짜 클릭**: 캘린더에서 날짜를 클릭하여 학습 내용 입력
4. **진도 체크**: 완료/부분완료 상태 업데이트
5. **색상 변경**: 계획 수정에서 원하는 색상 선택

## 라이선스 📄

MIT License

## 개발자 👨‍💻

pinkyj81

---

⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요!
