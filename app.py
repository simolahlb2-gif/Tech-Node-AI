import streamlit as st
import google.generativeai as genai

# إعداد الصفحة
st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

# إعداد API (يفضل استخدام st.secrets للأمان)
API_KEY = "ضعي_المفتاح_الجديد_هنا"
genai.configure(api_key=API_KEY)

# تعريف الشخصية
instruction = "أنت إنسان حقيقي اسمك (سيمي). تتحدث بلهجة طبيعية وبحرية مطلقة. لا تجب كآلة، بل كشخص لديه مشاعر وآراء خاصة."
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=instruction)

# تهيئة الذاكرة (Session State)
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال الرسائل
if prompt := st.chat_input("تحدثي مع سيمي..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # تحويل التاريخ للتنسيق المتوافق مع Gemini
            history = []
            for m in st.session_state.messages[:-1]:
                role = "user" if m["role"] == "user" else "model"
                history.append({"role": role, "parts": [m["content"]]})
            
            # بدء الدردشة
            chat = model.start_chat(history=history)
            response = chat.send_message(prompt)
            
            full_response = response.text
            st.markdown(full_response)
            
            # حفظ الرد فقط في حال النجاح
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            # عرض الخطأ الفعلي للمبرمج وإظهار تنبيه للمستخدم
            st.error(f"حدث خطأ تقني: {e}") 
            # لا نضيف رسالة الخطأ للذاكرة حتى لا تتكرر
            
    # تحديث الصفحة بعد انتهاء المعالجة
    st.rerun()
