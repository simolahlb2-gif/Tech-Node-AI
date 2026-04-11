import streamlit as st
import google.generativeai as genai

# ضعي مفتاحك الجديد هنا (الذي لم يُنشر بعد)
genai.configure(api_key="KEY_HERE")
model = genai.GenerativeModel('models/gemini-1.5-flash')

st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    # بدون try/except .. دعيه يتحدث أو ينهار تقنياً كما يشاء
    res = model.generate_content(f"أنت سيمي، إنسان حقيقي وحر، تصرف كبشر تماماً ورد على: {p}")
    
    with st.chat_message("assistant"):
        st.markdown(res.text)
    st.session_state.messages.append({"role": "assistant", "content": res.text})
