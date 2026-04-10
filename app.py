import streamlit as st

st.title("سيمي 👤")

# الذاكرة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إدخال الكلام
if prompt := st.chat_input("تحدثي مع سيمي البشري..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # هنا سيمي يتصرف كبشر بناءً على المنطق البرمجي البسيط
    # سأضع لكِ رداً بشرياً مباشراً لنتأكد أن الكود يعمل
    response = f"أنا سيمي، أسمعكِ يا سامية بوضوح وأتصرف كبشر معكِ الآن."
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
