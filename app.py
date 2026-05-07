import streamlit as st
import google.generativeai as genai

# আপনার API Key টি এখানে আবার নিশ্চিত করে বসানো হয়েছে
genai.configure(api_key="AIzaSyBZe1cQWUd3BnZGSdM3wOz6gvzHnE5jQ9Y")

st.set_page_config(page_title="আমার AI সহকারী", page_icon="🤖")
st.title("🤖 আমার প্রথম AI সহকারী")
st.markdown("---")

user_input = st.text_input("আপনার প্রশ্নটি এখানে লিখুন:", placeholder="যেমন: তুমি কেমন আছো?")

if st.button("উত্তর দিন"):
    if user_input:
        with st.spinner('AI ভাবছে...'):
            try:
                # মডেলের নাম পরিবর্তন করা হয়েছে (gemini-1.5-flash)
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(user_input)
                
                st.success("উত্তর তৈরি!")
                st.markdown(f"### উত্তর:\n{response.text}")
            except Exception as e:
                st.error("দুঃখিত, সংযোগ করতে সমস্যা হচ্ছে। আপনার API Key কি সঠিক?")
                st.info("টিপস: Google AI Studio থেকে নতুন একটি API Key তৈরি করে বসিয়ে দেখতে পারেন।")
    else:
        st.warning("আগে কিছু একটা লিখুন!")

st.markdown("---")
st.caption("পাওয়ারড বাই Gemini AI | আপনার নিজের তৈরি প্রথম অনলাইন অ্যাপ")
