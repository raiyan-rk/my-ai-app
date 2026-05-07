import streamlit as st
import google.generativeai as genai

# আপনার API Key এখানে সেট করা হয়েছে
genai.configure(api_key="AIzaSyBZe1cQWUd3BnZGSdM3wOz6gvzHnE5jQ9Y")

# অ্যাপের ইন্টারফেস ডিজাইন
st.set_page_config(page_title="আমার AI সহকারী", page_icon="🤖")
st.title("🤖 আমার প্রথম AI সহকারী")
st.markdown("---")

# ইউজার ইনপুট বক্স
user_input = st.text_input("আপনার প্রশ্নটি এখানে লিখুন:", placeholder="যেমন: আজকের দিনটি কেমন যাবে?")

# উত্তর দেওয়ার বাটন
if st.button("উত্তর দিন"):
    if user_input:
        with st.spinner('AI ভাবছে...'):
            try:
                # লেটেস্ট মডেল ব্যবহার করা হয়েছে
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(user_input)
                
                st.success("উত্তর তৈরি!")
                st.markdown(f"### উত্তর:\n{response.text}")
            except Exception as e:
                st.error("দুঃখিত, সংযোগ করতে সমস্যা হচ্ছে।")
    else:
        st.warning("আগে কিছু একটা লিখুন!")

# নিচে ছোট একটি ফুটনোট
st.markdown("---")
st.caption("পাওয়ারড বাই Gemini AI | আপনার নিজের তৈরি প্রথম অনলাইন অ্যাপ")
