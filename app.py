import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="MarketMinds AI", page_icon="🧠", layout="centered")

st.markdown("# 🧠 MarketMinds AI")
st.markdown("### Institutional-Grade Stock Analysis in 30 Seconds")
st.markdown("**5-Day AI Agent Intensive Capstone – Syed Mahfuz Hossain**")
st.markdown("---")

symbol = st.text_input("🔍 Enter Stock Ticker", "NVDA", help="e.g. AAPL, TSLA, AMD, BTC-USD")

if st.button("🚀 Generate Full Intelligence Report", type="primary", use_container_width=True):
    with st.spinner("5 AI Agents are working on your report..."):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        You are MarketMinds AI – a senior equity research analyst at Goldman Sachs.
        Perform a complete professional analysis on {symbol} and return a beautiful executive report including:
        • Current price & market trend
        • Top 3 competitors with threat level
        • Risk score (0-100) and category
        • Growth opportunities and strategic score
        • Final recommendation: STRONG BUY / BUY / HOLD / SELL
        Use professional formatting with emojis and bold text.
        """
        
        response = model.generate_content(prompt)
        
    st.success("Report Generated Successfully!")
    st.markdown(response.text)
    st.balloons()
    st.caption("Powered by Google Gemini 1.5 Flash • Deployed live for capstone bonus")
