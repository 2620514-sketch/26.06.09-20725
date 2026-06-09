import streamlit as st

st.set_page_config(page_title="긴급 호출 시스템", page_icon="🚨", layout="centered")

st.title("🚨 긴급 호출 시스템")
st.markdown("버튼을 3번 연속으로 눌러야 신고가 접수됩니다.")
st.divider()

if "fire_clicks" not in st.session_state:
    st.session_state.fire_clicks = 0
if "med_clicks" not in st.session_state:
    st.session_state.med_clicks = 0

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 화재 발생")
    if st.button("화재 신고", key="fire_btn", use_container_width=True):
        st.session_state.fire_clicks += 1
        if st.session_state.fire_clicks >= 3:
            st.error("🚨 [긴급] 화재 신고가 정상적으로 접수되었습니다!")
            st.session_state.fire_clicks = 0
        else:
            st.warning(f"오작동 방지: 앞으로 **{3 - st.session_state.fire_clicks}번** 더 누르면 화재 신고가 접수됩니다.")

with col2:
    st.subheader("🚑 응급 환자")
    if st.button("응급 의료 신고", key="med_btn", use_container_width=True):
        st.session_state.med_clicks += 1
        if st.session_state.med_clicks >= 3:
            st.success("🚑 [긴급] 응급 환자 신고가 정상적으로 접수되었습니다!")
            st.session_state.med_clicks = 0
        else:
            st.info(f"오작동 방지: 앞으로 **{3 - st.session_state.med_clicks}번** 더 누르면 응급 신고가 접수됩니다.")
