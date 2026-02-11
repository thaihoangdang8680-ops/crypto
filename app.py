import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Chiến Thần Soi Kèo", layout="wide")

# Lấy API Key
api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("Chưa có API Key!")
    st.stop()

genai.configure(api_key=api_key)

# Thử nghiệm kết nối với Model
try:
    # Bản này dùng model name ngắn gọn nhất
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Lỗi khởi tạo: {e}")

st.title("🚀 Chiến Thần Soi Kèo")

symbol = st.text_input("Nhập mã Coin (VD: BTCUSDT):", "BTCUSDT").upper()

if st.button("PHÂN TÍCH"):
    col1, col2 = st.columns([2, 1])
    with col1:
        # Biểu đồ TradingView chuẩn
        chart_html = f'<iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:{symbol}&interval=60&theme=dark" width="100%" height="500" frameborder="0"></iframe>'
        st.components.v1.html(chart_html, height=520)
    
    with col2:
        st.subheader("🤖 Dự báo từ AI")
        try:
            # Câu lệnh đơn giản để kiểm tra AI
            prompt = f"Phân tích {symbol}. Đưa ra Entry, TP, SL 3 khung thời gian trong biến động 1000-2000 điểm. Viết bằng tiếng Việt."
            response = model.generate_content(prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"AI đang bận hoặc lỗi: {e}")
