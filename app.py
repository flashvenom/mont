import streamlit as st
from db import init_db
from dotenv import load_dotenv
from components.chat import show_chat_section

load_dotenv()  # Add this at the top of app.py

def main():
    # Initialize the database
    init_db()
    
    st.set_page_config(
        page_title="My First Montessori - Health Insurance Portal",
        page_icon="🏥",
        layout="wide"
    )

    st.title("My First Montessori Health Insurance Center")
    
    # Initialize quotes in session state if not already done
    if 'pending_quotes' not in st.session_state:
        st.session_state.pending_quotes = {}  # Dict to store quotes by employee ID
    
    st.markdown("""
    ## How can we help you today?
    
    Choose from the following options:
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.warning("### My Benefits")
        st.write("View or change your existing health insurance benefits plan.")
        if st.button("Make Changes", key="changes"):
            st.switch_page("pages/2_Make_Changes.py")

    with col2:
        st.success("### Resources")
        st.write("Access helpful resources, contacts and documentation.")
        if st.button("View Resources", key="resources"):
            st.switch_page("pages/3_Resources.py")

    with col3:
        st.info("### New Enrollment")
        st.write("Start a new health insurance enrollment application.")
        if st.button("Start New Enrollment", key="new"):
            st.switch_page("pages/1_New_Enrollment.py")

    with col4:
        st.info("### Access My Quotes")
        st.write("View and select from your available quotes.")
        if st.button("Access Quotes", key="quotes"):
            st.switch_page("pages/4_Access_My_Quotes.py")
            

    # Quick Links Section
    st.markdown("### Quick Links")
    
    quick_links_col1, quick_links_col2 = st.columns(2)
    
    with quick_links_col1:
        st.markdown("""
        * [Find a Healthcare Provider](https://www.blueshieldca.com/fad/home)
        * [Contact HR Department](mailto:wendy@myfirstmontessori.com)
        """)
    
    with quick_links_col2:
        st.markdown("""
        * [Insurance Terms Glossary](http://files.metroinsurance.com/pdf/sbc/2025/glossary.pdf)
        * [Emergency Contact Information](mailto:wendy@myfirstmontessori.com)
        """)

    # Important Notices
    st.info("""
    **Important Notice**: Open enrollment period is from October 1st to December 15th. 
    Changes outside this period require a qualifying life event.
    """)

    # Add chat section at the bottom of the homepage
    show_chat_section()

if __name__ == "__main__":
    main() 