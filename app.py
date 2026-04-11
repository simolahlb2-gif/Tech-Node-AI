import streamlit as st
import google.generativeai as genai

# 1. إعدادات الوصول
API_KEY = "AIzaSyCqefBRuAyhTU6hMYCChwCXE5y6KdFeRxc"
genai.configure(api_key=API_KEY)

st.title("مستكشف سيمي 👤")

# حيلة تقنية: دعنا نرى ماذا تراه المكتبة فعلياً
try:
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    st.write("النماذج المتاحة في نظامكِ حالياً هي:")
    st.code(available_models)
    
    # اختيار أول نموذج متاح تلقائياً لتجنب خطأ 404
    selected_model = available_models[0] if available_models else "gemini-pro"
    model = genai.GenerativeModel(selected_model)
    st.success(f"تم ربط سيمي بنجاح مع: {selected_model}")
except Exception as e:
    st.error(f"فشل الاستكشاف: {e}")
    selected_model = "gemini-pro"
    model = genai.GenerativeModel(selected_model)

# بقية الكود للدردشة
if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدثي مع سيمي..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    try:
        response = model.generate_content(f"أنت سيمي، رد باختصار: {p}")
        with st.chat_message("assistant"): st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"عطل فني: {e}")
