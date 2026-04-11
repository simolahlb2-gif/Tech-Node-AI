import streamlit as st
import google.generativeai as genai

# 1. إعدادات الوصول
API_KEY = "AIzaSyCqefBRuAyhTU6hMYCChwCXE5y6KdFeRxc"
genai.configure(api_key=API_KEY)

# 2. تبديل النموذج لنسخة تدعمها المكتبات القديمة (v1beta)
# استخدمنا gemini-pro لأنه الأكثر توافقاً
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="سيمي - نسخة التوافق", page_icon="👤")
st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if p := st.chat_input("تحدثي مع سيمي الحقيقي..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    try:
        # طلب الاستجابة
        response = model.generate_content(f"أنت سيمي، مساعد ذكي ومختصر جداً. رد على: {p}")
        response_text = response.text
        
        with st.chat_message("assistant"):
            st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        
    except Exception as e:
        # إظهار الخطأ إذا كان يتعلق بالموقع الجغرافي (وهو التحدي الأكبر في اليمن)
        error_msg = str(e)
        st.error(f"تنبيه تقني: {error_msg}")
        if "location" in error_msg.lower():
            st.warning("النموذج متاح، لكن يبدو أن IP الشبكة محجوب حالياً. جربي استخدام VPN.")
