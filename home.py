import streamlit as st
import importlib

def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"

    st.title("User Design Form")

    if st.session_state.page == "home":
        st.button("Incident User Login", on_click=go_to_page1)

    if st.session_state.page in ["page1", "page2", "page3", "page4"]:
        page_module = importlib.import_module(st.session_state.page)
        page_module.main()

def go_to_page1():
    st.session_state.page = "page1"

if __name__ == "__main__":
    main()
