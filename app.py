import streamlit as st
from groq import Groq

# عنوان الموقع
st.set_page_config(page_title="Tech Node AI", page_icon="♟️")
st.title("Tech Node Independent")

# مفتاحك الجديد الذي يبدأ بـ gsk
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("System Ready..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # طلب الرد من المحرك الجديد
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
    except Exception as e:
        st.error(f"Logic Error: {str(e)}")
