import streamlit as st
import requests

st.set_page_config(page_title="SecureGPT", page_icon="🔒", layout="centered")

st.title("🔒 SecureGPT – فحص الرسائل والمخاطر الأمنية")
st.write("أدخل الرسالة أو الرابط المريب لتحليل محتواه الأمني:")

text = st.text_area("📩 الرسالة أو الرابط", height=150)

if st.button("🔍 فحص التهديد"):
    if text.strip() == "":
        st.warning("الرجاء إدخال نص للتحليل.")
    else:
        with st.spinner("جاري التحليل..."):
            try:
                response = requests.post("http://your-backend-url/analyze", json={"text": text})
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ تم التحليل بنجاح")
                    st.markdown(f"*مستوى التهديد:* {data['threat_level']}")
                    st.markdown(f"*نوع التهديد:* {data['threat_type']}")
                    st.markdown(f"*الشرح:* {data['explanation']}")
                    st.markdown(f"*التوصية:* 🛡 {data['action']}")

                    if data["google_evidence"]:
                        st.markdown("🔗 مصادر من Google:")
                        for link in data["google_evidence"]:
                            st.markdown(f"- [{link}]({link})")
                else:
                    st.error("حدث خطأ من الخادم.")
            except Exception as e:
                st.error(f"فشل الاتصال بالخادم: {e}")