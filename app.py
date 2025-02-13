import streamlit as st

def main():
    st.set_page_config(
        page_title="My First Montessori - Health Insurance Portal",
        page_icon="🏥",
        layout="wide"
    )

    st.title("Welcome to My First Montessori Health Insurance Portal")
    
    st.markdown("""
    ## How can we help you today?
    
    Choose from the following options:
    """)

    col1, col2, col3 = st.columns(3)

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