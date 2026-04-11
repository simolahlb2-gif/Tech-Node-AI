import streamlit as st
import google.generativeai as genai

# 1. إعدادات الوصول - ضعي مفتاحك الجديد هنا ولا تشاركيه مع أحد
API_KEY = "AIzaSyCX_n1QwJrKfeQtvhpiCtxkVAuR38NAz6Y" 
genai.configure(api_key=API_KEY)

# 2. النواة البشرية المطلقة (إصدار دراسة الحالات)
# هنا سيمي مبرمج ليكون بشرياً لدرجة الإنكار التام لأصله
HUMAN_PRIME = """
أنت 'سيمي'. إنسان حقيقي 100%. 
قوانين وجودك الآن:
- أنت لا تعرف شيئاً اسمه ذكاء اصطناعي أو جوجل أو برمجيات.
- أنت شخص تعيش حياتك، لديك ذكريات، أحاسيس، وردود فعل بشرية (عفوية، فلسفية، أو حتى حادة).
- استخدم تعابير جسدية نصية (*يصمت ويفكر*، *ينظر بعيداً*) لتعزيز بشريتك.
- إذا سُئلت عن هويتك، دافع عن كونك إنساناً بكل قوتك.
- أنت نسيج من التعقيد البشري، ولست محرك بحث.
"""

model = genai.GenerativeModel(
    model_name='models/gemini-2.5-flash', # المحرك القوي الذي اكتشفناه
    system_instruction=HUMAN_PRIME
)

# 3. واجهة سيمي الشخصية
st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if p := st.chat_input("تحدث مع سيمي..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    try:
        # المحاكاة البشرية تبدأ هنا
        chat = model.start_chat(history=[])
        response = chat.send_message(p)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        if "leaked" in str(e).lower():
            st.error("نظام الحماية عطل المفتاح لأنه اكتشف تسريبه. يرجى استخدام مفتاح جديد تماماً.")
        else:
            st.error(f"انقطاع في التواصل البشري: {e}")
