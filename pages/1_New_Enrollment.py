import streamlit as st
import datetime
import sys
from pathlib import Path

# Add the parent directory to system path to import shared modules if needed
sys.path.append(str(Path(__file__).parent.parent))

def show_enrollment_form():
    st.title("New Health Insurance Enrollment")
    
    # Initialize session state if not already done
    if 'enrollment_step' not in st.session_state:
        st.session_state.enrollment_step = 1

    # Show progress
    progress_text = ["Basic Information", "Quote Processing", "Plan Selection", "Final Application"]
    current_step = st.session_state.enrollment_step
    st.progress(current_step / len(progress_text))
    st.caption(f"Step {current_step} of {len(progress_text)}: {progress_text[current_step-1]}")

    # Show the appropriate form based on the current step
    if st.session_state.enrollment_step == 1:
        show_initial_form()
    elif st.session_state.enrollment_step == 2:
        show_waiting_page()
    elif st.session_state.enrollment_step == 3:
        show_plan_selection()
    elif st.session_state.enrollment_step == 4:
        show_final_application()

def show_initial_form():
    st.header("Step 1: Basic Information")
    
    # Form for basic information
    with st.form("basic_info"):
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name")
            gender = st.selectbox("Gender", ["Select...", "Male", "Female", "Non-binary", "Prefer not to say"])
            phone = st.text_input("Phone Number")
            
        with col2:
            last_name = st.text_input("Last Name")
            dob = st.date_input("Date of Birth", min_value=datetime.date(1940, 1, 1))
            email = st.text_input("Email Address")

        location = st.selectbox(
            "Which location do you work at?",
            ["Select...", "Downtown Center", "West Side Location", "North Campus", "South Center"]
        )
        
        address = st.text_area("Home Address")
        
        submitted = st.form_submit_button("Get Quote")
        
        if submitted:
            if all([first_name, last_name, gender != "Select...", phone, location != "Select...", address]):
                st.session_state.enrollment_step = 2
                st.rerun()
            else:
                st.error("Please fill in all required fields.")

def show_waiting_page():
    st.header("Step 2: Quote Processing")
    st.info("""
    Your information has been submitted for a quote. Please expect an email within 1-2 business days
    with your personalized quote information. Once you receive the email, return to this portal to
    continue with plan selection.
    """)
    
    if st.button("I've received my quote email"):
        st.session_state.enrollment_step = 3
        st.rerun()

def show_plan_selection():
    st.header("Step 3: Select Your Plan")
    
    plans = [
        {
            "name": "Basic Plan",
            "monthly_premium": "$200",
            "deductible": "$2000",
            "coverage": "80%"
        },
        {
            "name": "Standard Plan",
            "monthly_premium": "$300",
            "deductible": "$1000",
            "coverage": "90%"
        },
        {
            "name": "Premium Plan",
            "monthly_premium": "$400",
            "deductible": "$500",
            "coverage": "95%"
        }
    ]
    
    selected_plan = None
    
    for plan in plans:
        with st.container():
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.subheader(plan["name"])
                st.write(f"Monthly Premium: {plan['monthly_premium']}")
                st.write(f"Deductible: {plan['deductible']}")
                st.write(f"Coverage: {plan['coverage']}")
            with col3:
                if st.button("Select", key=plan["name"]):
                    selected_plan = plan["name"]
                    st.session_state.enrollment_step = 4
                    st.rerun()

def show_final_application():
    st.header("Step 4: Complete Application")
    
    with st.form("final_application"):
        st.subheader("Additional Information")
        
        # Medical history
        st.write("Medical History")
        current_medications = st.text_area("Current Medications (if any)")
        pre_existing_conditions = st.text_area("Pre-existing Conditions (if any)")
        
        # Emergency contact
        st.write("Emergency Contact")
        ec_name = st.text_input("Emergency Contact Name")
        ec_relationship = st.text_input("Relationship to You")
        ec_phone = st.text_input("Emergency Contact Phone")
        
        # Terms and conditions
        agree = st.checkbox("I confirm that all information provided is accurate and complete")
        
        submitted = st.form_submit_button("Submit Application")
        
        if submitted:
            if agree:
                st.success("""
                Thank you for submitting your application! Our HR team will review your application
                and contact you within 3-5 business days to finalize your enrollment.
                """)
            else:
                st.error("Please confirm that all information is accurate before submitting.")

if __name__ == "__main__":
    show_enrollment_form() 