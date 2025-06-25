import streamlit as st
import requests

st.set_page_config(
    page_title="URLNow | Free URL Shortener",
    page_icon="icon.png",
    menu_items={
        "About":"URLNow is a fast, reliable, and easy-to-use URL shortening service that helps you simplify long web addresses into short, shareable links."
    }
)

st.write("<h2 style='color:orange;'>Shorten Your URL Using URLNow.</h2>",unsafe_allow_html=True)

link = st.text_input("Paste the URL to be shortened",placeholder="Enter the link here")

btn = st.button("Shorten URL")
if btn:
    if not(link.startswith("http://") or link.startswith("https://")):
        st.info("⚠️ Please provide a valid URL beginning with http or https!")
    else:
        try:
            url = "https://url-shortener-service.p.rapidapi.com/shorten"
            payload = { "url": f"{link}" }
            headers = {
                "x-rapidapi-key": "c0e897e06bmshf1b07b02427bc79p1edb79jsn0132d0db5ef9",
                "x-rapidapi-host": "url-shortener-service.p.rapidapi.com",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            response = requests.post(url, data=payload, headers=headers)
            if response.status_code != 200:
                st.info("🥴 Failed to process the link!")
            else:
                data = response.json()
                if "result_url" in data:
                    st.code(data["result_url"])
                    st.toast("🔗 URL Shortened Successfully")
        except Exception as e:
            st.error("Something went wrong")