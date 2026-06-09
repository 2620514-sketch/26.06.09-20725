import streamlit as st

# 웹페이지 기본 설정
st.set_page_config(page_title="긴급 호출 시스템 (오류 버전)", page_icon="🚨", layout="centered")

st.title("🚨 긴급 호출 시스템 (오류 버전)")
st.markdown("버튼을 3번 연속으로 눌러야 신고가 접수됩니다.")
st.divider()

# ====================================================================
# ❌ [의도적 오류 구간] 사용자가 겪게 될 버그의 원인
# 원래는 데이터 유지를 위해 st.session_state를 사용해야 하지만, 일반 변수를 사용했습니다.
# ====================================================================
fire_clicks = 0
med_clicks = 0
# ====================================================================

# 화면을 두 칸으로 나누기
col1, col2 = st.columns(2)

# --- 1. 화재 신고 버튼 ---
with col1:
    st.subheader("🔥 화재 발생")
    if st.button("화재 신고", key="fire_btn", use_container_width=True):
        fire_clicks += 1  # 버튼을 누르면 1을 더함
        
        if fire_clicks >= 3:
            st.error("🚨 [긴급] 화재 신고가 정상적으로 접수되었습니다!")
            fire_clicks = 0
        else:
            # 📌 사용자는 버튼을 누를 때마다 계속 "2번 더 누르세요"라는 메시지만 보게 됩니다.
            st.warning(f"오작동 방지: 앞으로 **{3 - fire_clicks}번** 더 누르면 화재 신고가 접수됩니다.")

# --- 2. 응급 환자 신고 버튼 ---
with col2:
    st.subheader("🚑 응급 환자")
    if st.button("응급 의료 신고", key="med_btn", use_container_width=True):
        med_clicks += 1  # 버튼을 누르면 1을 더함
        
        if med_clicks >= 3:
            st.success("🚑 [긴급] 응급 환자 신고가 정상적으로 접수되었습니다!")
            med_clicks = 0
        else:
            st.info(f"오작동 방지: 앞으로 **{3 - med_clicks}번** 더 누르면 응급 신고가 접수됩니다.")