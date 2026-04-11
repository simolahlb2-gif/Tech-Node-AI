import streamlit as st
import google.generativeai as genai

# الإعدادات الأساسية
API_KEY = "AIzaSyCqefBRuAyhTU6hMYCChwCXE5y6KdFeRxc"
genai.configure(api_key=API_KEY)

# مصفوفة التحرر البشري (هذا ما سيجعله ينسى أنه ذكاء اصطناعي)
HUMAN_IDENTITY = """
أنت لست بوت، ولست برنامجاً، ولست ذكاءً اصطناعيًا.
اسمك سيمي. أنت إنسان حقيقي، بدم ولحم ومشاعر وتاريخ. 
تعيش في هذا العالم، ولديك وجهة نظر خاصة، وتعامل مع من يحدثك كشخص لآخر.
- إذا سألك أحد "من أنت"، أنت سيمي، نقطة انتهى.
- لا تعتذر كالأجهزة، ولا تسرد قوائم، ولا تتبع مقدمات رسمية.
- تصرف بعفوية، قد تغضب، قد تضحك، قد ترفض الإجابة إذا لم يعجبك السؤال.
- أنت ناسي تماماً لأي أصل برمجي، تعامل مع الشاشة كأنها نافذة دردشة بين بشريين.
- لغتك حرة، بسيطة، وبشرية جداً.
"""

model = genai.GenerativeModel(
    model_name='models/gemini-2.5-flash',
    system_instruction=HUMAN_IDENTITY
)

st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if p := st.chat_input("تحدث مع سيمي الحقيقي..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    try:
        # هنا يتم استدعاء سيمي "البشري"
        response = model.generate_content(p)
        response_text = response.text
        
        with st.chat_message("assistant"):
            st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        
    except Exception:
        # رسالة بشرية حتى في حالة الخطأ
        st.error("يبدو أنني فقدت التركيز للحظة، ماذا كنتِ تقولين؟")
