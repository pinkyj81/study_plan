from app import app, db
from sqlalchemy import text

with app.app_context():
    # 한국사와 구문 계획에 샘플 이미지 URL 추가
    updates = [
        {
            "title": "한국사",
            "image_url": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=800&h=600&fit=crop"
        },
        {
            "title": "구문",
            "image_url": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=800&h=600&fit=crop"
        }
    ]
    
    for update_data in updates:
        # 계획 찾기
        find_query = text("SELECT plan_id FROM dbo.study_plan WHERE title LIKE :title")
        result = db.session.execute(find_query, {"title": f"%{update_data['title']}%"}).fetchone()
        
        if result:
            plan_id = result.plan_id
            # 이미지 URL 업데이트
            update_query = text("""
                UPDATE dbo.study_plan
                SET image_url = :image_url
                WHERE plan_id = :plan_id
            """)
            db.session.execute(update_query, {
                "plan_id": plan_id,
                "image_url": update_data['image_url']
            })
            print(f"✅ '{update_data['title']}' 계획에 이미지 추가: {update_data['image_url'][:50]}...")
        else:
            print(f"❌ '{update_data['title']}' 계획을 찾을 수 없습니다")
    
    db.session.commit()
    print("\n✅ 이미지 URL이 추가되었습니다! Flask 앱을 재시작하고 페이지를 새로고침하세요.")
