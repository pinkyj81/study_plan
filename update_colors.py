from app import app, db, PLAN_COLORS
from sqlalchemy import text

with app.app_context():
    # 기존 계획들에 색상 할당
    plans = db.session.execute(text('SELECT plan_id FROM dbo.study_plan ORDER BY plan_id')).fetchall()
    
    for idx, plan in enumerate(plans):
        plan_id = plan.plan_id
        color_idx = (plan_id - 1) % len(PLAN_COLORS)
        color = PLAN_COLORS[color_idx]
        
        update_query = text("""
            UPDATE dbo.study_plan
            SET color = :color
            WHERE plan_id = :plan_id
        """)
        db.session.execute(update_query, {"plan_id": plan_id, "color": color})
        print(f'plan_id {plan_id}에 색상 {color} 할당')
    
    db.session.commit()
    print('\n✅ 모든 계획에 색상이 할당되었습니다!')
