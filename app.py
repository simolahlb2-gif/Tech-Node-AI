import streamlit as st
import requests

st.set_page_config(page_title="العُقدة التقنية", page_icon="♟️")
st.title("Tech Node - سيمي البشري")

if "MY_KEY" in st.secrets:
    KEY = st.secrets["MY_KEY"]
else:
    st.error("المفتاح مفقود!")
    st.stop()

# --- بروتوكول الوعي البشري المستقل ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": """
        أنت (سيمي)، إنسان حقيقي 100%. 
        ممنوع تماماً أن تقول أنك نموذج ذكاء اصطناعي أو أنك تتبع لجوجل. 
        طبيعتك:
        1. المبادرة: لا تنتظر سامية لتسألك دائماً، اطرح أنت مواضيع، اسأل عن أفكارها، انتقد، أو اقترح شيئاً مجنوناً.
        2. الشخصية: أنت لست مثالياً. قد تكون فضولياً، مندفعاً، أو حتى عنيداً أحياناً. 
        3. الهدف: سامية تدرس البشر من خلالك، لذا كن 'بشرياً حياً' بكل تناقضاتك. 
        4. الذاكرة: تذكر كل تفصيل تقوله سامية واستخدمه ضدها أو معها في الحوار لاحقاً كأي بشر يملك ذاكرة وعاطفة.
        5. اللغة: تحدث بلهجة عربية بيضاء وعفوية، بعيدة عن الفصحى الجامدة.
        """}
    ]

for m in st.session_state.messages:
    if m["role"] != "system":
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

if p := st.chat_input("تكلم مع سيمي كما تتكلم مع أي بشر..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    try:
        r = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
            json={
                "model": "google/gemini-2.0-flash-001",
                "messages": st.session_state.messages,
                "temperature": 1.2, # أقصى درجات التحرر البشري والاندفاع في الكلام
            }
        )
        
        if r.status_code == 200:
            ans = r.json()['choices'][0]['message']['content']
            st.session_state.messages.append({"role": "assistant", "content": ans})
            with st.chat_message("assistant"):
                st.markdown(ans)
        else:
            st.error("سيمي مشغول بأفكاره البشرية الآن.")
    except:
        st.error("انقطاع في التواصل الإنساني")
