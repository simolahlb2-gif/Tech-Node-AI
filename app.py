import streamlit as st
import os

st.title("Tech Node - Debug Mode 🛠️")

# هذا الكود سيخبرنا إذا كان الموقع يرى ملفاتك الجديدة أم لا
st.write("Checking System Files...")

if os.path.exists("requirements.txt"):
    st.success("✅ ملف المكتبات موجود")
else:
    st.error("❌ ملف requirements.txt مفقود أو مكتوب باسم خطأ")

st.write("Current Configuration:")
# سيظهر لنا آخر 4 أرقام من المفتاح لنتأكد أنه الجديد
OPENROUTER_API_KEY = "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"
st.code(f"Active Key ends with: ...{OPENROUTER_API_KEY[-4:]}")

st.info("يا سامية، إذا ظهرت العلامة الخضراء بالأعلى، فحظكِ ممتاز والماكينة بدأت تفهم.")
