from app import app, db
from sqlalchemy import text

with app.app_context():
    # 모든 계획 조회
    query = text("SELECT plan_id, title, subject FROM dbo.study_plan ORDER BY plan_id")
    plans = db.session.execute(query).fetchall()
    
    print("=== 현재 저장된 계획 목록 ===")
    for plan in plans:
        print(f"[{plan.plan_id}] {plan.title} (과목: {plan.subject})")
    
    print("\n샘플 이미지를 추가할 계획 ID를 입력하거나, 아래 명령으로 일괄 추가:")
    print("python add_multiple_images.py")
    
    # 샘플 이미지 목록
    sample_images = {
        "한국사": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=800",
        "기타": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=800",
        "수학": "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=800",
        "영어": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=800",
        "과학": "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=800",
    }
    
    # 과목 기반으로 자동 매칭
    updated_count = 0
    for plan in plans:
        subject = plan.subject if plan.subject else ""
        image_url = None
        
        # 과목명과 매칭
        for key, url in sample_images.items():
            if key in subject or key in plan.title:
                image_url = url
                break
        
        # 기본 이미지
        if not image_url:
            image_url = "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800"
        
        # 업데이트
        update_query = text("""
            UPDATE dbo.study_plan
            SET image_url = :image_url
            WHERE plan_id = :plan_id
        """)
        db.session.execute(update_query, {
            "plan_id": plan.plan_id,
            "image_url": image_url
        })
        updated_count += 1
        print(f"✅ [{plan.plan_id}] {plan.title} - 이미지 추가")
    
    db.session.commit()
    print(f"\n✅ 총 {updated_count}개 계획에 이미지가 추가되었습니다!")
    print("Flask 앱을 재시작하고 페이지를 새로고침(Ctrl+F5) 하세요.")
