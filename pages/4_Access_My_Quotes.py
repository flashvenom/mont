import streamlit as st

def show_quotes_page():
    st.title("Access My Quotes")
    
    st.header("Enter Your Quote Reference Number")
    
    quote_ref = st.text_input("Quote Reference Number")
    if st.button("Access Quote"):
        if quote_ref in st.session_state.get('pending_quotes', {}):
            st.session_state.current_quote = st.session_state.pending_quotes[quote_ref]
            st.session_state.enrollment_data = st.session_state.current_quote
            st.session_state.enrollment_step = 3
            st.switch_page("pages/1_New_Enrollment.py")
        else:
            st.error("Quote not found. Please check your reference number.")
    
    # Add option to go back
    st.markdown("---")
    if st.button("← Back to Homepage"):
        st.switch_page("app.py")

if __name__ == "__main__":
    show_quotes_page() 