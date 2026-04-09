import streamlit as st

st.set_page_config(page_title="عقدة التقنية", page_icon="♟️")
st.markdown("<h1 style='text-align: right;'>♟️ عقدة التقنية | Tech Node</h1>", unsafe_allow_html=True)
st.success("تم تفعيل النظام بنجاح يا سامية!")

if prompt := st.chat_input("أنا معكِ.. ماذا سنفعل اليوم؟"):
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write(f"نظام 'عقدة التقنية' استلم أمركِ: {prompt}")
