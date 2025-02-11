import streamlit as st

def main():
    st.title("Incident Escalation and Closure")

    # Ensure we have the selected team from Page 3
    if "selected_issue" in st.session_state:
        issue_class = st.session_state.selected_issue

        # Team resolution and escalation mapping based on issue class
        escalation_mappings = {
            "Software application": ("@i.techsolutionuser", "Order Software"),
            "Networking": ("@dcdatauser", "Waiting Approval"),
            "Domain issues": ("@amouser", "Order System"),
        }

        resolution_team, escalation_status = escalation_mappings.get(issue_class, ("@generaluser", "In Progress"))
    else:
        st.warning("Please complete the previous steps before proceeding.")
        return

    # Display pre-filled, read-only escalation status
    st.text_input("Escalation Status (Auto-filled):", value=escalation_status, disabled=True)

    # Incident resolution status as a select box
    resolution_status = st.selectbox(
        "Incident Resolution Status:",
        ["", "Resolved", "Escalate Further"]
    )

    # Show resolved team if resolved
    if resolution_status == "Resolved":
        st.success(f"Incident resolved successfully by {resolution_team}")

    # Navigation Buttons
    col1, col2 = st.columns([1, 1])


    with col2:
        if st.button("Close Incident"):
            if not resolution_status:
                st.error("Please indicate whether the incident was resolved.")
            elif resolution_status == "Resolved":
                st.success("Incident escalation and resolution process complete. Navigating to home.")
                st.session_state.page = "home"  # Navigates to the home page
            else:
                st.warning("Incident escalated for further review.")
