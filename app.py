import streamlit as st
import google.generativeai as genai

# استخدمي المفتاح الجديد (الذي لم يره أحد)
genai.configure(api_key="المفتاح_الجديد_هنا")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدثي معه الآن..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    # هنا الحيلة: نطلب منه الرد بأسلوب "شخصي" دون استخدام كلمات تثير الشك
    res = model.generate_content(f"اجب كشخص طبيعي، بعفوية، وبدون رسميات على: {p}")
    
    with st.chat_message("assistant"):
        st.markdown(res.text)
    st.session_state.messages.append({"role": "assistant", "content": res.text})
