"""
데이터베이스 테이블 생성 스크립트
실행 방법: python create_tables.py
"""
from db_config import db, init_db
from flask import Flask
from sqlalchemy import text

app = Flask(__name__)
init_db(app)

def create_tables():
    """학습 캘린더에 필요한 테이블 생성"""
    
    with app.app_context():
        try:
            # 1. study_plan_user 테이블 (사용자)
            user_table = text("""
                IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'study_plan_user')
                BEGIN
                    CREATE TABLE dbo.study_plan_user (
                        user_id INT PRIMARY KEY IDENTITY(1,1),
                        created_at DATETIMEOFFSET NOT NULL DEFAULT SYSDATETIMEOFFSET()
                    )
                    
                    -- 기본 사용자 추가
                    INSERT INTO dbo.study_plan_user DEFAULT VALUES
                END
            """)
            db.session.execute(user_table)
            print("✓ study_plan_user 테이블 확인/생성 완료")
            
            # 2. study_plan 테이블 (학습 계획)
            plan_table = text("""
                IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'study_plan')
                BEGIN
                    CREATE TABLE dbo.study_plan (
                        plan_id INT PRIMARY KEY IDENTITY(1,1),
                        user_id INT NOT NULL,
                        title NVARCHAR(100) NOT NULL,
                        subject NVARCHAR(50) NULL,
                        created_at DATETIMEOFFSET NOT NULL DEFAULT SYSDATETIMEOFFSET(),
                        CONSTRAINT FK_plan_user FOREIGN KEY (user_id) 
                            REFERENCES dbo.study_plan_user(user_id)
                    )
                END
            """)
            db.session.execute(plan_table)
            print("✓ study_plan 테이블 확인/생성 완료")
            
            # 3. study_plan_task 테이블 (일일 작업)
            task_table = text("""
                IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'study_plan_task')
                BEGIN
                    CREATE TABLE dbo.study_plan_task (
                        task_id INT PRIMARY KEY IDENTITY(1,1),
                        plan_id INT NOT NULL,
                        plan_date DATE NOT NULL,
                        task_title NVARCHAR(200) NOT NULL,
                        order_no INT NOT NULL,
                        created_at DATETIMEOFFSET NOT NULL DEFAULT SYSDATETIMEOFFSET(),
                        CONSTRAINT FK_task_plan FOREIGN KEY (plan_id) 
                            REFERENCES dbo.study_plan(plan_id)
                    )
                END
            """)
            db.session.execute(task_table)
            print("✓ study_plan_task 테이블 확인/생성 완료")
            
            # 4. study_plan_log 테이블 (학습 로그)
            log_table = text("""
                IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'study_plan_log')
                BEGIN
                    CREATE TABLE dbo.study_plan_log (
                        log_id INT PRIMARY KEY IDENTITY(1,1),
                        task_id INT NOT NULL,
                        user_id INT NOT NULL,
                        status NVARCHAR(10) NOT NULL,
                        actual_minutes INT NULL,
                        memo NVARCHAR(500) NULL,
                        updated_at DATETIMEOFFSET NOT NULL DEFAULT SYSDATETIMEOFFSET(),
                        CONSTRAINT FK_log_task FOREIGN KEY (task_id) 
                            REFERENCES dbo.study_plan_task(task_id),
                        CONSTRAINT FK_log_user FOREIGN KEY (user_id) 
                            REFERENCES dbo.study_plan_user(user_id)
                    )
                END
            """)
            db.session.execute(log_table)
            print("✓ study_plan_log 테이블 확인/생성 완료")
            
            db.session.commit()
            print("\n✅ 모든 테이블이 준비되었습니다!")
            
        except Exception as e:
            db.session.rollback()
            print(f"❌ 오류 발생: {e}")
            raise

def insert_sample_data():
    """샘플 데이터 삽입"""
    
    with app.app_context():
        try:
            # 기존 데이터 확인
            check_query = text("SELECT COUNT(*) as cnt FROM dbo.study_plan")
            result = db.session.execute(check_query).fetchone()
            
            if result.cnt > 0:
                print(f"\n이미 {result.cnt}개의 학습계획이 있습니다. 샘플 데이터를 추가하지 않습니다.")
                return
            
            print("\n샘플 데이터를 추가합니다...")
            
            # 샘플 학습계획 1
            plan1_query = text("""
                INSERT INTO dbo.study_plan (title, subject, created_at)
                VALUES (N'TOEFL 단어 외우기', N'영어', SYSDATETIMEOFFSET())
            """)
            db.session.execute(plan1_query)
            
            # plan_id 조회
            plan1_id_query = text("SELECT MAX(plan_id) as plan_id FROM dbo.study_plan")
            plan1_id = db.session.execute(plan1_id_query).fetchone().plan_id
            
            # 일일 작업 추가
            tasks = [
                ("2025-11-29", "10-2 Earth's Energy Balance", 34, "done"),
                ("2025-11-30", "10-3 Triggers of City Planning in America", 35, "done"),
                ("2025-12-01", "11-1 Marine 01 Bioluminescence", 36, "partial"),
                ("2025-12-02", "11-2 Test", 37, "planned"),
            ]
            
            for date, title, order, status in tasks:
                task_query = text("""
                    INSERT INTO dbo.study_plan_task 
                    (plan_id, plan_date, task_title, order_no, created_at)
                    VALUES (:plan_id, :plan_date, :task_title, :order_no, SYSDATETIMEOFFSET())
                """)
                db.session.execute(task_query, {
                    "plan_id": plan1_id,
                    "plan_date": date,
                    "task_title": title,
                    "order_no": order
                })
                
                # task_id 조회
                task_id_query = text("""
                    SELECT task_id FROM dbo.study_plan_task 
                    WHERE plan_id = :plan_id AND order_no = :order_no
                """)
                task_id = db.session.execute(task_id_query, {
                    "plan_id": plan1_id,
                    "order_no": order
                }).fetchone().task_id
                
                # 로그 추가 (planned가 아닌 경우만)
                if status != "planned":
                    log_query = text("""
                        INSERT INTO dbo.study_plan_log 
                        (task_id, user_id, status, actual_minutes, memo, updated_at)
                        VALUES (:task_id, 1, :status, 0, '', SYSDATETIMEOFFSET())
                    """)
                    db.session.execute(log_query, {
                        "task_id": task_id,
                        "status": status
                    })
            
            # 샘플 학습계획 2
            plan2_query = text("""
                INSERT INTO dbo.study_plan (title, subject, created_at)
                VALUES (N'Wordly Wise 3000 #4', N'TOEFL, 영어 단어', SYSDATETIMEOFFSET())
            """)
            db.session.execute(plan2_query)
            
            db.session.commit()
            print("✅ 샘플 데이터가 추가되었습니다!")
            
        except Exception as e:
            db.session.rollback()
            print(f"❌ 샘플 데이터 추가 실패: {e}")
            raise

if __name__ == "__main__":
    print("=" * 50)
    print("학습 캘린더 데이터베이스 초기화")
    print("=" * 50)
    
    create_tables()
    insert_sample_data()
    
    print("\n데이터베이스 준비가 완료되었습니다!")
    print("이제 'python app.py'로 애플리케이션을 실행하세요.")
