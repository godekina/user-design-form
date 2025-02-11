import streamlit as st

def main():
    st.title("Incident Log/Status")

    # Ensure we have the selected issue class from Page 2
    if "selected_issue" in st.session_state:
        issue_class = st.session_state.selected_issue

        # Mapping logic for team assignment and diagnosis action
        issue_mappings = {
            "Software application": ("Software Support Team", "Reinstall the software and check for updates", "resolved@i.techsolutionuser"),
            "Networking": ("Network Support Team", "Check router configurations and reset network", "resolved@dcdatauser"),
            "Domain issues": ("Domain Support Team", "Verify domain settings and rejoin the network", "resolved@amouser"),
        }
        
        assigned_team, diagnosis_action, resolution_email = issue_mappings.get(issue_class, 
            ("General Support Team", "Perform general diagnostics and system checks", "resolved@generaluser"))
    else:
        st.warning("Please complete the previous steps before proceeding.")
        return

    # Display pre-filled, read-only fields for assigned team and diagnosis action
    st.text_input("Assigned Team (Auto-filled):", value=assigned_team, disabled=True)
    st.text_area("Diagnosis Action (Auto-filled):", value=diagnosis_action, disabled=True)

    # Incident resolution status as a select box
    resolution_status = st.selectbox(
        "Incident Resolution Status:",
        ["", "Resolved", "Escalate"],
        index=0
    )

    col1, col2 = st.columns([1, 1])

    # Navigation Buttons with Resolution Handling
    with col1:
        if st.button("Back"):
            st.session_state.page = "page2"

    with col2:
        if st.button("Next"):
            if not resolution_status:
                st.error("Please select an incident resolution status before proceeding.")
            else:
                if resolution_status == "Resolved":
                    st.success(f"Incident resolved successfully. Resolution sent to {resolution_email} prees next to go back")
                    st.session_state.page = "home"
                else:
                    st.warning("Incident escalated. Moving to escalation details.")
                    st.session_state.page = "page4"
