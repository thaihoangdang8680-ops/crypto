import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Chiến Thần Soi Kèo", layout="wide")

api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("🚨 Thiếu API Key trong Secrets!")
    st.stop()

genai.configure(api_key=api_key)

# CẤU HÌNH MODEL CHUẨN
SYSTEM_PROMPT = "Bạn là chuyên gia Crypto. Dự báo Entry, TP, SL 3 khung thời gian."
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash', 
    system_instruction=SYSTEM_PROMPT
)

st.title("🚀 Chiến Thần Soi Kèo Crypto")

symbol = st.text_input("Nhập mã Coin:", "BTCUSDT").upper()

if st.button("PHÂN TÍCH"):
    try:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.subheader(f"📊 Biểu đồ {symbol}")
            chart_html = f'<iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:{symbol}&interval=60&theme=dark" width="100%" height="500"></iframe>'
            st.components.v1.html(chart_html, height=520)
        
        with col2:
            st.subheader("🤖 AI Dự Báo")
            with st.spinner("Đang soi cá mập..."):
                # Dùng phương thức gọi đơn giản nhất
                response = model.generate_content("Phân tích ngay!")
                st.markdown(response.text)
    except Exception as e:
        st.error(f"Lỗi: {e}")
        st.info("Mẹo: Nếu vẫn lỗi 404, bạn hãy thử đổi tên model trong code thành 'gemini-pro'")
