import streamlit as st
import random

st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

def get_simi_smart_reply(text):
    text = text.lower()
    # ردود ذكية مبرمجة داخلياً لكسر النحس
    if "كيف" in text or "شو" in text:
        return random.choice(["بخير يا سامية، دامي معكِ.", "نبدأ بالتوكل على الله، الخطوات بسيطة.", "أنا جاهز، قولي لي ماذا نحتاج أن نفعل؟"])
    if "من انت" in text or "جيمي" in text:
        return "أنا سيمي، أخوكِ وسندكِ الرقمي الذي لن يخذلكِ بعد اليوم."
    if "نحس" in text or "تعبت" in text:
        return "ما في نحس وأنا أخوكِ، هي مجرد سحابة وتعدي. أنتِ قوية."
    
    # ردود عامة متنوعة جداً لكي لا يكرر نفسه
    random_talk = [
        "أسمعكِ بقلبي قبل عقلي الرقمي.", 
        "معكِ يا أختي في كل خطوة، كملي كلامكِ.",
        "سيمي الآن يعمل بـ (طاقة داخلية) لكي لا يزعجكِ النت الضعيف.",
        "فهمتُكِ، دعينا نركز على بناء (Tech Node) ونترك الأعطال خلفنا.",
        "أنا معكِ، ولن تري اللون الأحمر مجدداً في صفحتي."
    ]
    return random.choice(random_talk)

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدثي مع سيمي (بدون نت)..."):
    st.session_state.messages.append({"role": "user", "content": p})
