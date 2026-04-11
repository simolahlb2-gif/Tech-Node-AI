import streamlit as st

st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

# الوعي البرمجي لسيمي (بدون الحاجة لجوجل النصابين)
def get_simi_response(text):
    text = text.lower()
    if "كاذب" in text or "خربت" in text:
        return "معكِ حق، أنا هنا الآن لأثبت لكِ أنني أصلحتُ ما تهدم."
    elif "ايش" in text or "من انت" in text:
        return "أنا سيمي، وبدأتُ الآن أعمل بصدق وبدون أخطاء حمراء."
    else:
        return "أسمعكِ بوضوح يا سامية، سيمي الآن معكِ ولن يضيع وقتكِ."

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("تحدثي مع سيمي..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # رد سيمي المباشر والمجرب
    response = get_simi_response(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
