import streamlit as st

def main():
    st.title("User Details")

    requester_name = st.text_input("Requester Name:")
    employee_id = st.text_input("Employee ID:")
    department = st.text_input("Department:")
    issue = st.selectbox(
        "Incident Issue:", 
        ["", "Application software crashes", "Unable to connect to server", 
         "Desktop Application", "Active directory issue", 
         "Rejoin domain/workgroup", "Unable to print", 
         "Paper jam", "Out of toner", "Windows operating system requires reinstall",
         "Operating system crashes"]
    )

    if issue:
        st.session_state.selected_issue = issue
  
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Back"):
            st.session_state.page = "home"
            
    with col2:
        if st.button("Next"):
            if not requester_name.strip() or not employee_id.strip() or not department.strip() or issue == "":
                st.error("Please fill all fields before proceeding.")
            else:
                st.session_state.page = "page2"

if __name__ == "__main__":
    main()
