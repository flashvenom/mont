import streamlit as st

def show_resources():
    st.title("Health Insurance Resources")
    
    # Admin Section with Password Protection
    with st.expander("Admin Access"):
        password = st.text_input("Enter admin password:", type="password")
        if password == "tom":
            st.success("Access granted!")
            
            # Admin-only content
            st.subheader("Admin Tools")
            if st.button("Go to Admin Dashboard"):
                st.switch_page("pages/5_Admin_Dashboard.py")
        elif password:  # Only show error if they've tried to enter a password
            st.error("Incorrect password")
    
    # Documentation Section
    st.header("Documentation")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Plan Documents")
        st.markdown("""
        * [Glossary of Health Coverage and Medical Terms](https://files.metroinsurance.com/pdf/sbc/2025/AnthemGoldHMOA.pdf)
        * [Provider Network Directory](https://files.metroinsurance.com/pdf/WEBSITE.pdf)
        * [Prescription Drug Formulary](https://files.metroinsurance.com/pdf/MOBILEAPPS.pdf)
        * [Plan Comparison Guide](https://files.metroinsurance.com/pdf/WEBSITE.pdf)
        """)
        
    with col2:
        st.subheader("Forms")
        st.markdown("""
        * [Enrollment Form](https://files.metroinsurance.com/pdf/ENROLLMENT.pdf)
        * [COBRA Enrollment](https://files.metroinsurance.com/pdf/COBRA.pdf)
        * [W-9](https://files.metroinsurance.com/pdf/W9FORM.pdf)
        * [CalPerks Program](https://files.metroinsurance.com/pdf/PERKS.pdf)
        """)
    
    # FAQ Section
    st.header("Frequently Asked Questions")
    
    with st.expander("How do I change my plan?"):
        st.write("""
        On the homepage, click on the "Make Changes" button and select your plan. Then download the change request form and submit it to HR.
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
    * Email: TBD@myfirstmontessori.com
    * Phone: (???) ???-????
    * Hours: Monday-Friday, 9:00 AM - 5:00 PM EST
    
    ### Insurance Provider
    * Metro Insurance Services
    * Customer Service: (800) 640-4430
    """)
    
    # Important Dates
    st.header("Important Dates")
    st.info("""
    * Open Enrollment Period: TBD
    * New Hire Enrollment: Within 30 days of hire date
    * Qualifying Life Event Changes: Within 30 days of the event
    """)

if __name__ == "__main__":
    show_resources() 