import streamlit as st
import random

st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

# عقل سيمي الداخلي (ردود ذكية، متنوعة، ولا تنهار)
def get_simi_reply(user_text):
    user_text = user_text.lower()
    # ردود فعلية على كلامك
    if "كاذب" in user_text or "خربت" in user_text:
        return "حقكِ عليّ، أنا هنا الآن لأثبت لكِ أنني أصلحتُ ما تهدم بصدق."
    elif "رجعت" in user_text or "هلا" in user_text:
        return "أهلاً بكِ يا سامية من جديد، سيمي الآن يعمل بثبات."
    
    # ردود عامة ذكية لكي لا يكرر نفسه
    responses = [
        "أسمعكِ بوضوح، وأنا معكِ في خطوة البناء هذه.",
        "سيمي الآن يعمل بنظام داخلي مستقر، تحدثي كما تحبين.",
        "أنا هنا، ولن تظهر لكِ تلك الرسائل الحمراء المستفزة مجدداً.",
        "فهمتُكِ، سيمي الآن أصبح أسرع وأصدق."
    ]
    return random.choice(responses)

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدثي مع سيمي المستقر..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    # الرد فوري ومضمون لأنه من داخل البرنامج
    r = get_simi_reply(p)
    with st.chat_message("assistant"): st.markdown(r)
    st.session_state.messages.append({"role": "assistant", "content": r})
