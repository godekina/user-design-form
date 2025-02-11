import streamlit as st

def main():
    st.title("Incident Log and Status")

    # Ensure we have the selected issue from previous steps
    if "selected_issue" in st.session_state:
        issue_class = st.session_state.selected_issue
    else:
        st.warning("Please complete the previous steps before proceeding.")
        return

    # Team assignment selection
    assigned_team = st.selectbox(
        "Select Assigned Team:",
        ["Select Team", "Software Team", "Network Team", "Domain  Team", "Support Team"],
        index=0
    )

    # Diagnosis action input
    diagnosis_action = st.text_area(
        "Diagnosis Action:",
        placeholder="E.g., Checked the server logs and identified connection timeout."
    )

    # Incident resolution status selection
    resolution_status = st.selectbox(
        "Incident Resolution Status:",
        ["Select Status", "Resolved", "Escalate"],
        index=0
    )

    # Navigation Buttons with Resolution Handling
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Back"):
            st.session_state.page = "page2"

    with col2:
        if st.button("Next"):
            if assigned_team == "Select Team":
                st.error("Please select an assigned team before proceeding.")
            elif not diagnosis_action.strip():
                st.error("Please enter a diagnosis action before proceeding.")
            elif resolution_status == "Select Status":
                st.error("Please select a resolution status.")
            elif resolution_status == "Resolved":
                st.success("Incident resolved successfully. Returning to homepage.")
                st.session_state.page = "home"
            else:
                st.warning("Incident escalated. Moving to escalation details.")
                st.session_state.page = "page4"
