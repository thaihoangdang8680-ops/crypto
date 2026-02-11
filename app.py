import streamlit as st
import google.generativeai as genai

# Cấu hình trang
st.set_page_config(page_title="Chiến Thần Soi Kèo", layout="wide")

# Lấy API Key từ Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("🚨 Thiếu API Key! Hãy vào Settings -> Secrets để dán Key vào nhé.")
    st.stop()

genai.configure(api_key=api_key)

# Dùng model phiên bản ổn định nhất
SYSTEM_PROMPT = "Bạn là chuyên gia phân tích Crypto. Hãy đưa ra dự báo Entry, TP, SL 3 khung thời gian cho mã coin người dùng nhập."
model = genai.GenerativeModel(model_name='gemini-1.5-flash', system_instruction=SYSTEM_PROMPT)

st.title("🚀 Chiến Thần Soi Kèo Crypto")

symbol = st.text_input("Nhập mã Coin (VD: BTCUSDT):", "BTCUSDT").upper()

if st.button("PHÂN TÍCH"):
    try:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.subheader(f"📊 Biểu đồ {symbol}")
            chart_html = f'<iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_765e2&symbol=BINANCE:{symbol}&interval=H&hidesidetoolbar=1&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=[]&theme=dark&style=1&timezone=Asia%2FHo_Chi_Minh" width="100%" height="500" frameborder="0" allowfullscreen></iframe>'
            st.components.v1.html(chart_html, height=520)
        
        with col2:
            st.subheader("🤖 AI Dự Báo")
            with st.spinner("Đang soi cá mập..."):
                # Gửi yêu cầu phân tích
                response = model.generate_content(f"Phân tích {symbol} ngay!")
                st.markdown(response.text)
    except Exception as e:
        st.error(f"Lỗi rồi bạn hiền ơi: {e}")
