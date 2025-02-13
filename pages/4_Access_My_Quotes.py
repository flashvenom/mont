import streamlit as st
from db import get_db
import datetime

def get_demo_quotes():
    return [
        {
            "carrier": "Kaiser Permanente",
            "type": "HMO",
            "plan_name": "Silver HMO D",
            "network": "Full",
            "monthly_premium": "$291.10",
            "cost_per_period": "$68.05",
            "sort_value": 68.05
        },
        {
            "carrier": "Kaiser Permanente",
            "type": "HMO",
            "plan_name": "Silver HMO C",
            "network": "Full",
            "monthly_premium": "$310.46",
            "cost_per_period": "$77.73",
            "sort_value": 77.73
        },
        {
            "carrier": "Kaiser Permanente",
            "type": "HMO",
            "plan_name": "Silver HMO B",
            "network": "Full",
            "monthly_premium": "$317.78",
            "cost_per_period": "$81.39",
            "sort_value": 81.39
        },
        {
            "carrier": "United Healthcare",
            "type": "HMO",
            "plan_name": "Gold HMO B",
            "network": "Full",
            "monthly_premium": "$379.17",
            "cost_per_period": "$112.09",
            "sort_value": 112.09
        },
        {
            "carrier": "Kaiser Permanente",
            "type": "HMO",
            "plan_name": "Gold HMO B_Kaiser",
            "network": "Full",
            "monthly_premium": "$391.99",
            "cost_per_period": "$118.50",
            "sort_value": 118.50
        },
        {
            "carrier": "United Healthcare",
            "type": "HMO",
            "plan_name": "Gold HMO A",
            "network": "Signature Value",
            "monthly_premium": "$391.99",
            "cost_per_period": "$118.50",
            "sort_value": 118.50
        },
        {
            "carrier": "Anthem Blue Cross",
            "type": "PPO",
            "plan_name": "Gold PPO B",
            "network": "SelectPPO",
            "monthly_premium": "$410.91",
            "cost_per_period": "$127.40",
            "sort_value": 127.40
        }
    ]

def show_quotes_page():
    st.title("Access My Quotes")
    
    # Debug: Show session state
    st.write("Debug - Session State:", st.session_state)
    
    # Initialize session state
    if 'enrollment_step' not in st.session_state:
        st.session_state.enrollment_step = 1
    if 'enrollment_data' not in st.session_state:
        st.session_state.enrollment_data = {}
    
    st.info("""
    Enter your quote reference number to view your insurance quotes. 
    """)
    
    st.header("Enter Your Quote Reference Number")
    
    # Store quote_ref in session state to persist between reruns
    if 'quote_ref_input' not in st.session_state:
        st.session_state.quote_ref_input = ""
    
    quote_ref = st.text_input("Quote Reference Number", 
                             key="quote_ref_input",
                             value=st.session_state.quote_ref_input)
    
    # Debug: Show current input
    st.write("Debug - Current quote_ref:", quote_ref)
    
    if st.button("Access Quote"):
        st.write("Debug - Button clicked")
        try:
            # Get application and quotes from database
            conn = get_db()
            c = conn.cursor()
            
            # First check if application exists
            c.execute("""
                SELECT id, quote_ref, first_name, last_name, gender, phone, email, dob, location, address 
                FROM applications 
                WHERE quote_ref = ?
            """, (quote_ref,))
            application = c.fetchone()
            
            # Debug: Show application lookup result
            st.write("Debug - Application found:", application is not None)
            if application:
                st.write("Debug - Application details:", application)
                
                # Get quotes for this application
                c.execute("""
                    SELECT COUNT(*) FROM quotes WHERE application_id = ?
                """, (application[0],))
                
                quote_count = c.fetchone()[0]
                st.write("Debug - Quote count:", quote_count)
                
                # If no quotes exist, generate them
                if quote_count == 0:
                    from db import save_quotes
                    save_quotes(application[0], get_demo_quotes())
                    st.write("Debug - Generated new quotes")
                
                # Store in session state for plan selection
                st.session_state.enrollment_data = {
                    'id': application[0],
                    'quote_ref': application[1],
                    'first_name': application[2],
                    'last_name': application[3],
                    'gender': application[4],
                    'phone': application[5],
                    'email': application[6],
                    'dob': application[7],
                    'location': application[8],
                    'address': application[9],
                    'quotes': get_demo_quotes()
                }
                
                # Set step to plan selection
                st.session_state.enrollment_step = 3
                st.write("Debug - Set enrollment step to 3")
                
                # Close connection before switching
                conn.close()
                
                # Switch to enrollment page
                st.write("Debug - About to switch page")
                st.switch_page("pages/1_New_Enrollment.py")
            else:
                st.error("Quote reference not found. Please check your number and try again.")
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.write("Error details:", str(e))
        finally:
            if 'conn' in locals():
                conn.close()

    # Add option to go back
    st.markdown("---")
    if st.button("← Back to Homepage"):
        st.switch_page("app.py")

if __name__ == "__main__":
    show_quotes_page() 