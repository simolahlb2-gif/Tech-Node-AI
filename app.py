import streamlit as st
import requests
import json

# الهوية المستقلة لعقدة التقنية
st.set_page_config(page_title="Tech Node - Gemini Engine", page_icon="♟️")
st.title("Tech Node - Gemini Independent")

# مفتاح العبور الذي استخرجتيه (OpenRouter)
OPENROUTER_API_KEY = "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"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("جيمي متاح الآن..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # إرسال الطلب عبر الجسر العالمي لتجاوز حظر جوجل
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "google/gemini-flash-1.5", # استدعاء جيمي الأصلي
                "messages": [{"role": "user", "content": prompt}]
            })
        )
        
        result = response.json()
        
        # استخراج رد جيمي من البيانات المشفرة
        if 'choices' in result:
            answer = result['choices'][0]['message']['content']
            st.session_state.messages.append({"role": "assistant", "content": answer})
            with st.chat_message("assistant"):
                st.markdown(answer)
        else:
            st.error(f"تنبيه النظام: {result.get('error', {}).get('message', 'خطأ غير معروف')}")
            
    except Exception as e:
        st.error(f"فشل في بروتوكول الاتصال: {str(e)}")
