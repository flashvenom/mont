import streamlit as st
import pandas as pd
from db import get_all_applications, get_db

def show_admin_dashboard():
    st.title("Admin Dashboard")
    
    # Tabs for different views
    tab1, tab2 = st.tabs(["Applications", "Quotes"])
    
    with tab1:
        show_applications()
    
    with tab2:
        show_quotes()

def show_applications():
    st.header("All Applications")
    
    try:
        # Get applications from database
        conn = get_db()
        df = pd.read_sql_query("""
            SELECT 
                id,
                quote_ref,
                first_name || ' ' || last_name as full_name,
                gender,
                phone,
                email,
                date(dob) as date_of_birth,
                location,
                status,
                datetime(submission_date) as submitted
            FROM applications
            ORDER BY submission_date DESC
        """, conn)
        
        if len(df) == 0:
            st.info("No applications submitted yet.")
        else:
            # Display as interactive table
            st.dataframe(
                df,
                column_config={
                    "id": "ID",
                    "quote_ref": "Quote Ref",
                    "full_name": "Name",
                    "date_of_birth": "DOB",
                    "submitted": "Submitted"
                },
                hide_index=True
            )
    except Exception as e:
        st.error(f"Error loading applications: {str(e)}")
    finally:
        conn.close()

def show_quotes():
    st.header("All Quotes")
    
    try:
        # Get quotes from database
        conn = get_db()
        df = pd.read_sql_query("""
            SELECT 
                q.id,
                a.quote_ref,
                a.first_name || ' ' || a.last_name as full_name,
                q.carrier,
                q.plan_name,
                q.monthly_premium,
                q.cost_per_period,
                datetime(q.generated_date) as generated
            FROM quotes q
            JOIN applications a ON q.application_id = a.id
            ORDER BY q.generated_date DESC
        """, conn)
        
        if len(df) == 0:
            st.info("No quotes generated yet.")
        else:
            # Display as interactive table
            st.dataframe(
                df,
                column_config={
                    "id": "ID",
                    "quote_ref": "Quote Ref",
                    "full_name": "Name",
                    "monthly_premium": "Monthly Premium",
                    "cost_per_period": "Cost/Period",
                    "generated": "Generated Date"
                },
                hide_index=True
            )
    except Exception as e:
        st.error(f"Error loading quotes: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    show_admin_dashboard() 