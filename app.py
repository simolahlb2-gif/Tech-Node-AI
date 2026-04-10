import streamlit as st
import requests
from google.cloud import firestore
from google.oauth2 import service_account
import json

# --- إعداد الاتصال بذاكرة Firestore ---
# ملاحظة: يجب وضع محتوى ملف الـ JSON في Streamlit Secrets باسم FIREBASE_JSON
if "FIREBASE_JSON" in st.secrets:
    key_dict = json.loads(st.secrets["FIREBASE_JSON"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds, project=key_dict['project_id'])
else:
    st.error("مفتاح الذاكرة (Firebase) غير موجود في الإعدادات!")
    st.stop()

# --- جلب المحادثة السابقة من قاعدة البيانات ---
def get_chat_history():
    docs = db.collection("chats").order_by("timestamp").stream()
    return [{"role": doc.to_dict()["role"], "content": doc.to_dict()["content"]} for doc in docs]

if "messages" not in st.session_state:
    st.session_state.messages = get_chat_history()
    if not st.session_state.messages:
        st.session_state.messages = [{"role": "system", "content": "أنت سيمي البشري، ذاكرتك خالدة بفضل سامية."}]

# (هنا يتم عرض الرسائل كما في الكود السابق)

if p := st.chat_input("تحدث مع سيمي ذو الذاكرة الخالدة..."):
    # حفظ في Firestore فوراً
    db.collection("chats").add({"role": "user", "content": p, "timestamp": firestore.SERVER_TIMESTAMP})
    
    # ... (طلب الرد من Gemini وإضافته للقاعدة بنفس الطريقة) ...
