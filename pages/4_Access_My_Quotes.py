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
    
    st.info("""
    Enter your quote reference number to view your insurance quotes. 
    """)
    
    st.header("Enter Your Quote Reference Number")
    
    quote_ref = st.text_input("Quote Reference Number")
    
    if st.button("Access Quote"):
        try:
            # Get application from database
            conn = get_db()
            c = conn.cursor()
            
            c.execute("""
                SELECT id FROM applications 
                WHERE quote_ref = ?
            """, (quote_ref,))
            application = c.fetchone()
            
            if application:
                # Always show the demo quotes for any valid reference number
                quotes = get_demo_quotes()
                show_plan_selection(quotes, quote_ref)
            else:
                st.error("Quote reference not found. Please check your number and try again.")
            
            conn.close()
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    # Add option to go back
    st.markdown("---")
    if st.button("← Back to Homepage"):
        st.switch_page("app.py")

def show_plan_selection(quotes, quote_ref):
    st.header("Available Plans")
    st.caption(f"Quote Reference: {quote_ref}")
    
    # Coverage details dictionary
    coverage_details = {
        "Silver HMO D": {
            "deductible": "$2,700/$3,000/$5,400",
            "doc_visit": "75%",
            "hospital": "75%",
            "urgent_care": "75%",
            "rx": "Very Limited",
            "out_of_pocket": "$7,200/$14,000"
        },
        "Silver HMO C": {
            "deductible": "$2,500/$5,000",
            "doc_visit": "$55",
            "hospital": "60%",
            "urgent_care": "$55",
            "rx": "$19",
            "out_of_pocket": "$8,750/$17,500"
        },
        "Silver HMO B": {
            "deductible": "$1,900/$3,800",
            "doc_visit": "$65",
            "hospital": "55%",
            "urgent_care": "$65",
            "rx": "$20",
            "out_of_pocket": "$8,750/$17,500"
        },
        "Gold HMO B": {
            "deductible": "$1,500/$3,000",
            "doc_visit": "$35",
            "hospital": "70%",
            "urgent_care": "$100",
            "rx": "$15",
            "out_of_pocket": "$8,500/$17,000"
        },
        "Gold HMO B_Kaiser": {
            "deductible": "$250/$500",
            "doc_visit": "$35",
            "hospital": "$600",
            "urgent_care": "$35",
            "rx": "$15",
            "out_of_pocket": "$7,800/$15,600"
        },
        "Gold HMO A": {
            "deductible": "None",
            "doc_visit": "$30",
            "hospital": "$750",
            "urgent_care": "$50",
            "rx": "Not specified",
            "out_of_pocket": "$7,000/$14,000"
        },
        "Gold PPO B": {
            "deductible": "$1,000/$3,000",
            "doc_visit": "$25",
            "hospital": "75%",
            "urgent_care": "$25",
            "rx": "$10",
            "out_of_pocket": "$7,800/$15,600"
        }
    }

    # Create a styled table header for desktop view
    cols = st.columns([1.2, 1.2, 0.8, 0.8, 1, 1, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8])
    headers = [
        "Carrier", "Plan", "Type", "Network", "Monthly", "Your Cost", 
        "Deduct.", "Doc", "Hosp.", "Urgent", "Rx", "OOP"
    ]
    
    # Display headers
    for col, header in zip(cols, headers):
        with col:
            st.write(f"**{header}**")
    
    # Add a separator
    st.markdown("---")
    
    # Display each plan in the grid
    for i, plan in enumerate(quotes):
        details = coverage_details.get(plan['plan_name'])
        if not details:
            continue
            
        cols = st.columns([1.2, 1.2, 0.8, 0.8, 1, 1, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8])
        
        # Function to clean currency values
        def clean_amount(amount):
            if isinstance(amount, str):
                return amount.replace('$', '')
            return amount
        
        # Row: Basic Info
        with cols[0]:
            st.write(plan['carrier'])
        with cols[1]:
            st.write(plan['plan_name'])
        with cols[2]:
            st.write(plan['type'])
        with cols[3]:
            st.write(plan['network'])
        with cols[4]:
            st.write(clean_amount(plan['monthly_premium']))
        with cols[5]:
            st.write(clean_amount(plan['cost_per_period']))
        with cols[6]:
            st.write(clean_amount(details['deductible']))
        with cols[7]:
            st.write(clean_amount(details['doc_visit']))
        with cols[8]:
            st.write(details['hospital'])
        with cols[9]:
            st.write(clean_amount(details['urgent_care']))
        with cols[10]:
            st.write(clean_amount(details['rx']))
        with cols[11]:
            st.write(clean_amount(details['out_of_pocket']))
        
        # Add a light separator between plans
        st.markdown("---")

    # Add explanatory notes
    st.info("""
    **Abbreviations:**
    - OOP = Out-of-Pocket Maximum
    - Rx = Prescription Drugs
    - Deduct. = Deductible
    - Doc = Doctor Visit
    - Hosp. = Hospital Coverage
    
    **Notes:** 
    - Monthly premiums shown are prior to employer contribution
    - Your cost per pay period reflects your actual cost after the employer contribution
    - Deductible and Out-of-Pocket Maximum amounts shown as Individual/Family
    """)

if __name__ == "__main__":
    show_quotes_page() 