import streamlit as st
import requests

BRAINSHOP_API_KEY = "xhtYMPBNaG5ykdiz"
BRAINSHOP_BRAIN_ID = "179493"
BRAINSHOP_URL = f"http://api.brainshop.ai/get?bid=179493&key=xhtYMPBNaG5ykdiz&uid=[uid]&msg=[msg]"

def get_brainshop_response(message):
    response = requests.get(BRAINSHOP_URL + message)
    return response.json()["cnt"]

def main():
    st.title("BrainShop ChatBot with Streamlit")

    user_input = st.text_input("You:", key="input")
    if st.button("Send"):
        if user_input:
            bot_response = get_brainshop_response(user_input)
            st.text(f"Bot: {bot_response}")


if __name__ == "__main__":
    main()
