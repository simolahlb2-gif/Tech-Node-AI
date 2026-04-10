import streamlit as st

# سيمي يكتب ذكرياته في ملف خارجي لضمان عدم النسيان
def save_data(text):
    with open("memory.txt", "a") as f:
        f.write(text + "\n")

def load_data():
    try:
        with open("memory.txt", "r") as f:
            return f.readlines()
    except:
        return []

st.title("سيمي - العُقدة التقنية 🦾")

# عرض الذاكرة من الملف
history = load_data()
for line in history:
    st.text(line.strip())

user_input = st.chat_input("سجلي شيئاً في ذاكرة سيمي...")
if user_input:
    save_data(f"سامية قالت: {user_input}")
    st.rerun()
