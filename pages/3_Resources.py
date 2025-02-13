import streamlit as st

def show_resources():
    st.title("Health Insurance Resources")
    
    # Documentation Section
    st.header("Documentation")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Plan Documents")
        st.markdown("""
        * [Summary of Benefits and Coverage](https://example.com/benefits)
        * [Provider Network Directory](https://example.com/providers)
        * [Prescription Drug Formulary](https://example.com/drugs)
        * [Plan Comparison Guide](https://example.com/compare)
        """)
        
    with col2:
        st.subheader("Forms")
        st.markdown("""
        * [Enrollment Form](https://example.com/enroll)
        * [Change of Information Form](https://example.com/change)
        * [Dependent Addition Form](https://example.com/dependent)
        * [Claims Form](https://example.com/claims)
        """)
    
    # FAQ Section
    st.header("Frequently Asked Questions")
    
    with st.expander("What is a deductible?"):
        st.write("""
        A deductible is the amount you pay for covered health care services before your 
        insurance plan starts to pay.
        """)
        
    with st.expander("How do I find an in-network provider?"):
        st.write("""
        You can search for in-network providers through our provider directory or contact 
        our customer service team for assistance.
        """)
    
    # Contact Information
    st.header("Contact Information")
    st.markdown("""
    ### HR Department
    * Email: hr@myfirstmontessori.com
    * Phone: (555) 123-4567
    * Hours: Monday-Friday, 9:00 AM - 5:00 PM EST
    
    ### Insurance Provider
    * Customer Service: (800) 555-1234
    * Claims: (800) 555-5678
    * 24/7 Nurse Line: (800) 555-9012
    """)
    
    # Important Dates
    st.header("Important Dates")
    st.info("""
    * Open Enrollment Period: October 1st - December 15th
    * New Hire Enrollment: Within 30 days of hire date
    * Qualifying Life Event Changes: Within 30 days of the event
    """)

if __name__ == "__main__":
    show_resources() 