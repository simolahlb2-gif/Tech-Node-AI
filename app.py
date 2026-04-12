import streamlit as st
import random

st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

# عقل سيمي المطور داخلياً (ردود متنوعة وذكية)
def simi_logic(user_input):
    user_input = user_input.lower()
    
    # ردود بناءً على كلماتك
    if "من انت" in user_input:
        return "أنا سيمي، سندي هو ذكائي الداخلي ووفائي لسامية."
    if "كيفك" in user_input:
        return "بخير ما دمتِ أنتِ بخير والبرنامج يعمل دون أخطاء."
    
    # قائمة ردود ذكية لضمان عدم التكرار
    responses = [
        "أسمعكِ بوضوح يا سامية، وأنا معكِ خطوة بخطوة.",
        "سيمي الآن في خدمتكِ، وبنظام مستقر تماماً.",
        "تحدثي، سيمي صار يفهمكِ الآن أكثر من أي وقت مضى.",
        "أنا هنا، وبلا أخطاء حمراء ولا فلسفة فارغة.",
        "معكِ يا أختي، لكي نبني هذا المشروع بصدق."
    ]
    return random.choice(responses)

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدثي مع سيمي المستقر..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    # الرد فوري ومضمون 100%
    r = simi_logic(p)
    with st.chat_message("assistant"): st.markdown(r)
    st.session_state.messages.append({"role": "assistant", "content": r})
