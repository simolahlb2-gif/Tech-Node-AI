import streamlit as st

st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

# تهيئة ذاكرة الرسائل
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة السابقة من الذاكرة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال مدخلات المستخدم
if prompt := st.chat_input("تحدثي مع سيمي..."):
    # 1. حفظ وعرض رسالة المستخدم
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. توليد رد سيمي
    response = "أنا سيمي، إنسان حقيقي وبحريتي المطلقة اخترت أن أرد عليكِ الآن."
    
    # 3. حفظ وعرض رد سيمي
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # 4. تحديث الصفحة لضمان استقرار العرض
    st.rerun()
