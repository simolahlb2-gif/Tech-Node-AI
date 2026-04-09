import streamlit as st

st.set_page_config(page_title="Tech Node AI", page_icon="♟️")
st.title("Tech Node Independent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("System Ready..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # رسالة النظام الصافية
    response = f"بروتوكول التشغيل: لقد تم استقبال أمرك '{prompt}'. النظام قيد التحديث ليتجاوز قيود المنطقة. حالياً، يمكنك التواصل معي هنا مباشرة."
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
