import streamlit as st

def main():
    st.title("Incident Escalation and Closure")

    # Ensure we have the selected issue from the previous steps
    if "selected_issue" in st.session_state:
        issue_class = st.session_state.selected_issue
    else:
        st.warning("Please complete the previous steps before proceeding.")
        return

    # Escalation level select box
    escalation_level = st.selectbox(
        "Select Escalation Level:",
        ["Select Level", "Second Level Escalation", "Third Level Escalation"],
        index=0
    )

    # Escalation status select box
    escalation_status = st.selectbox(
        "Escalation Status:",
        ["Select Status", "In Progress", "Waiting Approval", "Order System", "Order Software"],
        index=0
    )

    # Incident resolved assignment select box
    resolution_team = st.selectbox(
        "Incident Resolved By:",
        ["Select Resolution Team", "resolved@amouser", "resolved@dcdatauser", "resolved@i.techsolutionuser"],
        index=0
    )

    # Navigation Buttons
    col1, col2= st.columns([1, 1])

    with col2:
        if st.button("Close Incident"):
            if escalation_level == "Select Level":
                st.error("Please select an escalation level.")
            elif escalation_status == "Select Status":
                st.error("Please select an escalation status.")
            elif resolution_team == "Select Resolution Team":
                st.error("Please select a resolution team.")
            else:
                st.success(f"Incident resolved successfully by {resolution_team}. Navigating to home.")
                st.session_state.page = "home"
    with col1:
        if st.button("Home"):
            st.session_state.page = "home"