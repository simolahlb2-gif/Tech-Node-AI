import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
import json

# دالة ذكية للاتصال بالقاعدة
def init_db():
    try:
        # التأكد من وجود المفتاح في Secrets
        if "FIREBASE_JSON" not in st.secrets:
            st.error("المفتاح مفقود تماماً من Secrets!")
            return None
        
        # تحويل النص إلى قاموس برمي
        info = json.loads(st.secrets["FIREBASE_JSON"])
        creds = service_account.Credentials.from_service_account_info(info)
        return firestore.Client(credentials=creds, project=info['project_id'])
    except Exception as e:
        st.error(f"حدث خطأ في قراءة المفتاح: {e}")
        return None

db = init_db()

st.title("سيمي - الذاكرة المطورة 🧠")

if db:
    st.success("تم الاتصال بذاكرة سيمي بنجاح!")
    # هنا يكمل باقي كود المحادثة...
else:
    st.warning("سيمي الآن 'بلا وعي'.. يرجى ضبط المفتاح في Secrets.")
