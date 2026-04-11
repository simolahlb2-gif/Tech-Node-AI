import streamlit as st
import google.generativeai as genai

# 1. إعدادات الوصول الآمن - تم دمج المفتاح الجديد
API_KEY = "AIzaSyCqefBRuAyhTU6hMYCChwCXE5y6KdFeRxc"
genai.configure(api_key=API_KEY)

# 2. تهيئة النموذج المطور (Gemini 1.5 Flash)
# هذا النموذج أسرع وأكثر استقراراً في المناطق ذات الإنترنت المحدود
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. إعدادات واجهة المستخدم (تنسيق Tech Node)
st.set_page_config(page_title="سيمي - النسخة الاحترافية", page_icon="👤")
st.title("سيمي 👤")

# 4. نظام إدارة الذاكرة (لضمان عدم تكرار الردود)
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثات السابقة بشكل منظم
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# 5. معالجة المدخلات وتوليد الاستجابة
if p := st.chat_input("تحدثي مع سيمي الحقيقي..."):
    # إضافة مدخلات المستخدم للسجل
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    # محاولة توليد الرد
    try:
        # هندسة الأوامر لضمان شخصية ذكية ومختصرة
        response = model.generate_content(f"أنت سيمي، مساعد ذكي، منطقي، ومختصر جداً. رد على: {p}")
        response_text = response.text
        
        # عرض رد النظام وحفظه
        with st.chat_message("assistant"):
            st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        
    except Exception as e:
        # في حال حدوث خطأ، سيظهر السبب الحقيقي بالإنجليزية لتسهيل حله
        st.error(f"حدث خطأ تقني: {str(e)}")
        if "location" in str(e).lower():
            st.warning("تنبيه: يبدو أن هناك قيوداً جغرافية على الوصول. قد تحتاجين لتشغيل VPN أو استخدام بروكسي.")
