import streamlit as st
from db import init_db

def main():
    # Initialize the database
    init_db()
    
    st.set_page_config(
        page_title="My First Montessori - Health Insurance Portal",
        page_icon="🏥",
        layout="wide"
    )

    st.title("Welcome to the Metro/Montessori Health Insurance Portal")
    
    # Initialize quotes in session state if not already done
    if 'pending_quotes' not in st.session_state:
        st.session_state.pending_quotes = {}  # Dict to store quotes by employee ID
    
    st.markdown("""
    ## How can we help you today?
    
    Choose from the following options:
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("### New Enrollment")
        st.write("Start a new health insurance enrollment application.")
        if st.button("Start New Enrollment", key="new"):
            st.switch_page("pages/1_New_Enrollment.py")

    with col2:
        st.warning("### Make Changes")
        st.write("Update your existing health insurance plan or information.")
        if st.button("Make Changes", key="changes"):
            st.switch_page("pages/2_Make_Changes.py")

    with col3:
        st.info("### Access My Quotes")
        st.write("View and select from your available quotes.")
        if st.button("Access Quotes", key="quotes"):
            st.switch_page("pages/4_Access_My_Quotes.py")
            
    with col4:
        st.success("### Resources")
        st.write("Access helpful resources and documentation.")
        if st.button("View Resources", key="resources"):
            st.switch_page("pages/3_Resources.py")

    # Quick Links Section
    st.markdown("---")
    st.markdown("### Quick Links")
    
    quick_links_col1, quick_links_col2 = st.columns(2)
    
    with quick_links_col1:
        st.markdown("""
        * [Understanding Your Benefits](https://example.com/benefits)
        * [Find a Healthcare Provider](https://example.com/providers)
        * [Contact HR Department](mailto:hr@myfirstmontessori.com)
        """)
    
    with quick_links_col2:
        st.markdown("""
        * [Insurance Terms Glossary](https://www.healthcare.gov/glossary/)
        * [FAQ](https://example.com/faq)
        * [Emergency Contact Information](https://example.com/emergency)
        """)

    # Important Notices
    st.markdown("---")
    st.info("""
    **Important Notice**: Open enrollment period is from October 1st to December 15th. 
    Changes outside this period require a qualifying life event.
    """)

if __name__ == "__main__":
    main() 