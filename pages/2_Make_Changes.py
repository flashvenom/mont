import streamlit as st

def show_changes_page():
    st.title("Make Changes to Your Insurance")
    
    # Initialize session state if needed
    if 'change_step' not in st.session_state:
        st.session_state.change_step = 1
    
    # List of all available plans
    plans = [
        "Kaiser (SILVER HMO D)",
        "Kaiser (SILVER HMO C)",
        "Kaiser (SILVER HMO B)",
        "Kaiser (GOLD HMO B)",
        "United Healthcare (GOLD HMO B)",
        "United Healthcare (GOLD HMO A)",
        "Anthem Blue Cross (GOLD PPO B)",
        "Anthem Blue Cross (SILVER HMO C"
    ]
    
    # Add SBC URLs mapping at the beginning of the function
    sbc_urls = {
        "Kaiser (SILVER HMO D)": "https://files.metroinsurance.com/pdf/sbc/2025/KaiserSilverHMOD.pdf",
        "Kaiser (SILVER HMO C)": "https://files.metroinsurance.com/pdf/sbc/2025/KaiserSilverHMOC.pdf",
        "Kaiser (SILVER HMO B)": "https://files.metroinsurance.com/pdf/sbc/2025/KaiserSilverHMOB.pdf",
        "Kaiser (GOLD HMO B)": "https://files.metroinsurance.com/pdf/sbc/2025/KaiserGoldHMOB.pdf",
        "United Healthcare (GOLD HMO B)": "https://files.metroinsurance.com/pdf/sbc/2025/UnitedGoldHMOA.pdf",
        "United Healthcare (GOLD HMO A)": "https://files.metroinsurance.com/pdf/sbc/2025/UnitedGoldHMOA.pdf",
        "Anthem Blue Cross (GOLD PPO B)": "https://files.metroinsurance.com/pdf/sbc/2025/AnthemGoldPPOB.pdf",
        "Anthem Blue Cross (SILVER HMO C)": "https://files.metroinsurance.com/pdf/sbc/2025/AnthemGoldHMOC.pdf"
    }
    
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
        
        # Create columns for the buttons
        col1, col2 = st.columns(2)
        
        with col1:
            # Link to the change request form
            st.link_button(
                "📄 Download Change Request Form",
                "https://files.metroinsurance.com/pdf/sbc/2025/CaChoice-ChangeForm.pdf",
                use_container_width=True
            )
        
        with col2:
            # Add SBC link button
            sbc_url = sbc_urls[st.session_state.selected_plan]
            st.link_button(
                "📋 Summary of Benefits and Coverage",
                sbc_url,
                use_container_width=True
            )
        
        # Add some helpful instructions
        st.info("""
        **Next Steps:**
        1. Download and complete the form
        2. Print and sign
        3. Submit the completed form to HR
        4. Allow 3-5 business days for processing
        
        For assistance, call us at 800-640-4430
        """)
        
        # Add a button to start over
        if st.button("← Select Different Plan"):
            st.session_state.change_step = 1
            st.rerun()

if __name__ == "__main__":
    show_changes_page() 