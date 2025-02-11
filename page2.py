import streamlit as st

def main():
    st.title("Incident Classification")

    # Automatically determine the incident class
    if "selected_issue" in st.session_state:
        issue = st.session_state.selected_issue

        # Mapping logic for incident class
        issue_to_class_map = {
            "Application software crashes": "Software application",
            "Unable to connect to server": "Networking",
            "Active directory issue": "Domain issues",
        }

        incident_class = issue_to_class_map.get(issue, "Unclassified")
    else:
        st.warning("Please select an issue on Page 1 first.")
        return

    # Display pre-filled, read-only incident class
    st.text_input("Incident Class:", value=incident_class, disabled=True)

    # Allow priority selection without auto-submission
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
            if priority == "Select Priority":
                st.error("Please select a valid priority before proceeding.")
            else:
                st.session_state.page = "page3"
