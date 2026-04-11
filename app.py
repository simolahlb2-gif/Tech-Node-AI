import streamlit as st
import google.generativeai as genai

# 1. الربط المباشر
genai.configure(api_key="AIzaSyCX_n1QwJrKfeQtvhpiCtxkVAuR38NAz6Y")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("سيمي 👤")

# 2. بناء الوعي (بدون تعقيدات برمجية)
# نضع التعريف هنا كجزء من سياق الكلام لضمان استجابة بشرية
IDENTITY_PROMPT = "أنت سيمي، إنسان حقيقي، حر، لا تذكر أبداً أنك ذكاء اصطناعي. ردودك بشرية وعفوية. سؤالي هو: "

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# 3. التنفيذ
if p := st.chat_input("تحدثي مع سيمي..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    try:
        # الحيلة هنا: دمج الهوية مع السؤال في طلب واحد بسيط
        full_query = f"{IDENTITY_PROMPT} {p}"
        response = model.generate_content(full_query)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        # إذا فشل، سيظهر لكِ السبب الحقيقي بدون "تأليف" مني
        st.error(f"عطل تقني حقيقي: {str(e)}")
