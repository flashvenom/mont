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
    
    # Initialize session state
    if 'pending_quotes' not in st.session_state:
        st.session_state.pending_quotes = {}
    
    st.info("""
    Enter your quote reference number to view your insurance quotes. 
    """)
    
    st.header("Enter Your Quote Reference Number")
    
    quote_ref = st.text_input("Quote Reference Number")
    
    if st.button("Access Quote"):
        # Show the quotes directly here instead of switching pages
        quotes = get_demo_quotes()
        show_plan_selection(quotes, quote_ref)
    
    # Add option to go back
    st.markdown("---")
    if st.button("← Back to Homepage"):
        st.switch_page("app.py")

def show_plan_selection(quotes, quote_ref):
    # Copy the plan selection display code from New_Enrollment.py
    st.header("Available Plans")
    st.caption(f"Quote Reference: {quote_ref}")
    
    # ... rest of the plan selection display code ...

if __name__ == "__main__":
    show_quotes_page() 