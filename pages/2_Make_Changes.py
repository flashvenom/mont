import streamlit as st

def show_changes_page():
    st.title("Make Changes to Your Insurance")
    
    # Initialize session state if needed
    if 'change_step' not in st.session_state:
        st.session_state.change_step = 1
    
    # List of all available plans
    plans = [
        "Kaiser Silver HMO D",
        "Kaiser Silver HMO C",
        "Kaiser Silver HMO B",
        "United Healthcare Gold HMO B",
        "Kaiser Gold HMO B",
        "United Healthcare Gold HMO A",
        "Anthem Blue Cross Gold PPO B"
    ]
    
    if st.session_state.change_step == 1:
        st.header("Which plan are you currently on?")
        
        # Create two columns for better layout
        col1, col2 = st.columns(2)
        
        # Split plans between columns
        mid_point = len(plans) // 2 + len(plans) % 2
        
        with col1:
            for plan in plans[:mid_point]:
                if st.button(plan, key=f"btn_{plan}", use_container_width=True):
                    st.session_state.selected_plan = plan
                    st.session_state.change_step = 2
                    st.rerun()
                st.write("")  # Add some spacing between buttons
        
        with col2:
            for plan in plans[mid_point:]:
                if st.button(plan, key=f"btn_{plan}", use_container_width=True):
                    st.session_state.selected_plan = plan
                    st.session_state.change_step = 2
                    st.rerun()
                st.write("")  # Add some spacing between buttons
    
    elif st.session_state.change_step == 2:
        st.header("Your Change Request Form Is Here:")
        
        # Display selected plan
        st.write(f"Current Plan: **{st.session_state.selected_plan}**")
        
        # Create a download button for the form
        # Note: In a real application, you would generate a specific form based on the plan
        st.download_button(
            label="📄 Download Change Request Form",
            data=b"Placeholder for actual form data",  # Replace with actual form data
            file_name="change_request_form.pdf",
            mime="application/pdf"
        )
        
        # Add some helpful instructions
        st.info("""
        **Next Steps:**
        1. Download and complete the form
        2. Submit the completed form to HR
        3. Allow 3-5 business days for processing
        
        For assistance, contact HR at hr@myfirstmontessori.com
        """)
        
        # Add a button to start over
        if st.button("← Select Different Plan"):
            st.session_state.change_step = 1
            st.rerun()

if __name__ == "__main__":
    show_changes_page() 