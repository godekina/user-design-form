import streamlit as st

def main():
    st.title("Incident Classification")

    # Incident Classification Select Box
    incident_class = st.selectbox(
        "Incident Classification:",
        ["Select Classification", "Software application", "Networking", "Domain issues"],
        index=0
    )

    # Incident Priority Select Box
    priority = st.selectbox(
        "Incident Priority:",
        ["Select Priority", "Low", "Medium", "High"],
        index=0
    )

    # Navigation Buttons
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Back"):
            st.session_state.page = "page1"

    with col2:
        if st.button("Next"):
            if incident_class == "Select Classification":
                st.error("Please select a valid incident classification before proceeding.")
            elif priority == "Select Priority":
                st.error("Please select a valid priority before proceeding.")
            else:
                st.session_state.selected_classification = incident_class
                st.session_state.page = "page3"
