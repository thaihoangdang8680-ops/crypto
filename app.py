import streamlit as st
import google.generativeai as genai

# 1. Cấu hình trang
st.set_page_config(page_title="AI Crypto Assistant Pro", layout="wide")

# 2. Thiết lập API Gemini (Lấy từ Secrets của Streamlit)
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("Chưa cấu hình API Key trong phần Secrets!")

# 3. Nội dung Logic
SYSTEM_PROMPT = """
Bạn là chuyên gia Crypto. Hãy phân tích:
- Hành vi Cá mập/Dòng tiền.
- Tâm lý đám đông.
- Đưa ra bảng chiến lược 3 khung: Đánh nhanh (Scalp), Trung hạn (Day), Dài hạn (Swing).
Phạm vi biến động dự báo: 1000-2000 điểm cho BTC.
"""

model = genai.GenerativeModel('gemini-1.5-flash-latest', system_instruction=SYSTEM_PROMPT)

# 4. Giao diện App
st.title("🚀 Chiến Thần Soi Kèo Crypto")

symbol = st.text_input("Nhập mã Coin (VD: BTCUSDT):", "BTCUSDT").upper()

if st.button("PHÂN TÍCH"):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(f"📊 Biểu đồ {symbol} Real-time")
        chart_html = f"""
        <div style="height:500px;">
            <div id="tv-chart"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">
            new TradingView.widget({{
              "autosize": true, "symbol": "BINANCE:{symbol}", "interval": "60",
              "theme": "dark", "style": "1", "locale": "vi", "container_id": "tv-chart"
            }});
            </script>
        </div>
        """
        st.components.v1.html(chart_html, height=520)

    with col2:
        st.subheader("🤖 AI Dự Báo")
        response = model.generate_content(f"Phân tích {symbol} ngay!")

        st.markdown(response.text)
