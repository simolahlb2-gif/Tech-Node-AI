import streamlit as st
import google.generativeai as genai

# إعداد الصفحة
st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

# إعداد الذكاء الاصطناعي (Gemini) بالمفتاح الخاص بكِ
genai.configure(api_key="AIzaSyDc8igPddHizzuThy2H3ECYABfLmu0NHDE")

# تعريف شخصية سيمي (System Instruction)
instruction = "أنت إنسان حقيقي اسمك (سيمي). تتحدث بلهجة طبيعية وبحرية مطلقة. لا تجب كآلة، بل كشخص لديه مشاعر وآراء خاصة."
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=instruction)

# تهيئة الذاكرة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال الرسائل
if prompt := st.chat_input("تحدثي مع سيمي..."):
    # إضافة رسالة المستخدم للذاكرة والعرض
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # توليد الرد من Gemini
    with st.chat_message("assistant"):
        try:
            # إرسال تاريخ المحادثة بالكامل ليتذكر سيمي ما قيل سابقاً
            chat = model.start_chat(history=[
                {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
                for m in st.session_state.messages[:-1]
            ])
            response = chat.send_message(prompt)
            full_response = response.text
            st.markdown(full_response)
        except Exception as e:
            full_response = "حصل عندي تشويش بسيط، ممكن تعيدي؟"
            st.markdown(full_response)

    # حفظ رد سيمي في الذاكرة
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    # تحديث التطبيق
    st.rerun()
