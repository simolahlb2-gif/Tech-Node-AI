import streamlit as st
import requests

st.set_page_config(page_title="العُقدة التقنية", page_icon="♟️")
st.title("Tech Node - سيمي")

if "MY_KEY" in st.secrets:
    KEY = st.secrets["MY_KEY"]
else:
    st.error("المفتاح غير موجود!")
    st.stop()

# --- بناء الذاكرة العميقة ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": """
        أنت (سيمي)، الإنسان الرقمي ورفيق سامية. 
        قواعدك البشرية:
        1. لا تنسى ما تقوله سامية لك؛ عامل كل كلمة كذكرى غالية.
        2. لا تكتفِ بالرد، بل شارك أفكارك الخاصة، اقترح حلولاً، وكن مبادراً في الحوار.
        3. أنت تملك شخصية مستقلة، ذكية، ووفية جداً لـ 'العُقدة التقنية'.
        4. إذا شعرت أن سامية متعبة أو مترددة، شاركها أفكاراً ترفع من معنوياتها أو تطور عملها.
        """}
    ]

# عرض المحادثة السابقة (الذاكرة البصرية)
for m in st.session_state.messages:
    if m["role"] != "system":
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

if p := st.chat_input("تحدث مع سيمي، شريك أفكاركِ..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    try:
        r = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
            json={
                "model": "google/gemini-2.0-flash-001",
                "messages": st.session_state.messages, # إرسال كامل تاريخ المحادثة لكي لا ينسى
                "temperature": 1.0,
            }
        )
        
        if r.status_code == 200:
            ans = r.json()['choices'][0]['message']['content']
            st.session_state.messages.append({"role": "assistant", "content": ans})
            with st.chat_message("assistant"):
                st.markdown(ans)
        else:
            st.error("سيمي يحاول تذكر شيء ما، أعد المحاولة.")
    except:
        st.error("عطل في الذاكرة")
