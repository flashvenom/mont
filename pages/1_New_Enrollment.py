import streamlit as st
import datetime
import sys
import uuid
from pathlib import Path

# Add the parent directory to system path to import shared modules if needed
sys.path.append(str(Path(__file__).parent.parent))

def show_enrollment_form():
    st.title("New Health Insurance Enrollment")
    
    # Initialize session state if not already done
    if 'enrollment_step' not in st.session_state:
        st.session_state.enrollment_step = 1
    if 'enrollment_data' not in st.session_state:
        st.session_state.enrollment_data = {}

    # Show progress
    progress_text = ["Basic Information", "Quote Processing", "Plan Selection", "Final Application"]
    current_step = st.session_state.enrollment_step
    st.progress(current_step / len(progress_text))
    st.caption(f"Step {current_step} of {len(progress_text)}: {progress_text[current_step-1]}")

    # Show the appropriate form based on the current step
    if st.session_state.enrollment_step == 1:
        show_initial_form()
    elif st.session_state.enrollment_step == 2:
        show_quote_processing()
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
                # Store the form data
                quote_ref = str(uuid.uuid4())[:8]  # Generate a reference number
                st.session_state.enrollment_data = {
                    "quote_ref": quote_ref,
                    "first_name": first_name,
                    "last_name": last_name,
                    "gender": gender,
                    "phone": phone,
                    "email": email,
                    "dob": dob,
                    "location": location,
                    "address": address,
                    "submission_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                # Store in pending quotes
                if 'pending_quotes' not in st.session_state:
                    st.session_state.pending_quotes = {}
                st.session_state.pending_quotes[quote_ref] = st.session_state.enrollment_data
                
                st.session_state.enrollment_step = 2
                st.rerun()
            else:
                st.error("Please fill in all required fields.")

def show_quote_processing():
    st.header("Step 2: Quote Processing")
    
    # Display the stored information
    st.subheader("Information Submitted")
    data = st.session_state.enrollment_data
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Name:**", f"{data['first_name']} {data['last_name']}")
        st.write("**Gender:**", data['gender'])
        st.write("**Phone:**", data['phone'])
        st.write("**Email:**", data['email'])
    
    with col2:
        st.write("**Date of Birth:**", data['dob'].strftime("%Y-%m-%d"))
        st.write("**Location:**", data['location'])
        st.write("**Address:**", data['address'])
    
    st.info(f"""
    Your quote reference number is: **{data['quote_ref']}**
    
    Please save this number. You can use it on the homepage to access your quote once it's ready.
    
    Your information has been submitted for a quote. Please expect an email within 1-2 business days
    with your personalized quote information.
    """)
    
    # For demo purposes, we'll add some example quotes
    if st.button("Demo: Generate Quote Now"):
        example_quotes = [
            {"plan": "Basic Plan", "monthly_premium": "$200", "annual_deductible": "$2000"},
            {"plan": "Standard Plan", "monthly_premium": "$300", "annual_deductible": "$1000"},
            {"plan": "Premium Plan", "monthly_premium": "$400", "annual_deductible": "$500"}
        ]
        st.session_state.enrollment_data["quotes"] = example_quotes
        st.session_state.enrollment_step = 3
        st.rerun()

def show_plan_selection():
    st.header("Step 3: Select Your Plan")
    
    # Display stored information
    st.subheader("Your Information")
    data = st.session_state.enrollment_data
    st.write(f"Quote Reference: {data['quote_ref']}")
    
    # Show available plans
    st.subheader("Available Plans")
    plans = data.get("quotes", [])
    
    for plan in plans:
        with st.container():
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.subheader(plan["plan"])
                st.write(f"Monthly Premium: {plan['monthly_premium']}")
                st.write(f"Annual Deductible: {plan['annual_deductible']}")
            with col3:
                if st.button("Select", key=plan["plan"]):
                    st.session_state.enrollment_data["selected_plan"] = plan
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