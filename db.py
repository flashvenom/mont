import sqlite3
import datetime
from pathlib import Path

def init_db():
    db_path = Path("insurance.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Create tables
    c.executescript("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote_ref TEXT UNIQUE,
            first_name TEXT,
            last_name TEXT,
            gender TEXT,
            phone TEXT,
            email TEXT,
            dob DATE,
            location TEXT,
            address TEXT,
            submission_date DATETIME,
            status TEXT DEFAULT 'PENDING',
            selected_plan_id INTEGER,
            current_medications TEXT,
            pre_existing_conditions TEXT,
            ec_name TEXT,
            ec_relationship TEXT,
            ec_phone TEXT
        );
        
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            application_id INTEGER,
            carrier TEXT,
            plan_type TEXT,
            plan_name TEXT,
            network TEXT,
            monthly_premium DECIMAL(10,2),
            cost_per_period DECIMAL(10,2),
            generated_date DATETIME,
            FOREIGN KEY (application_id) REFERENCES applications (id)
        );
        
        CREATE TABLE IF NOT EXISTS plan_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plan_name TEXT UNIQUE,
            deductible TEXT,
            doc_visit TEXT,
            hospital TEXT,
            urgent_care TEXT,
            rx TEXT,
            out_of_pocket TEXT
        );
    """)
    
    # Insert default plan details if not exists
    plan_details = [
        ("Silver HMO D", "$2,700/$3,000/$5,400", "75%", "75%", "75%", "Very Limited", "$7,200/$14,000"),
        ("Silver HMO C", "$2,500/$5,000", "$55", "60%", "$55", "$19", "$8,750/$17,500"),
        ("Silver HMO B", "$1,900/$3,800", "$65", "55%", "$65", "$20", "$8,750/$17,500"),
        ("Gold HMO B", "$1,500/$3,000", "$35", "70%", "$100", "$15", "$8,500/$17,000"),
        ("Gold HMO B_Kaiser", "$250/$500", "$35", "$600", "$35", "$15", "$7,800/$15,600"),
        ("Gold HMO A", "None", "$30", "$750", "$50", "Not specified", "$7,000/$14,000"),
        ("Gold PPO B", "$1,000/$3,000", "$25", "75%", "$25", "$10", "$7,800/$15,600")
    ]
    
    c.executemany("""
        INSERT OR IGNORE INTO plan_details 
        (plan_name, deductible, doc_visit, hospital, urgent_care, rx, out_of_pocket)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, plan_details)
    
    conn.commit()
    conn.close()

def get_db():
    db_path = Path("insurance.db")
    return sqlite3.connect(db_path)

# Application functions
def save_application(data):
    conn = get_db()
    c = conn.cursor()
    
    c.execute("""
        INSERT INTO applications 
        (quote_ref, first_name, last_name, gender, phone, email, dob, location, address, submission_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data['quote_ref'],
        data['first_name'],
        data['last_name'],
        data['gender'],
        data['phone'],
        data['email'],
        data['dob'],
        data['location'],
        data['address'],
        datetime.datetime.now()
    ))
    
    application_id = c.lastrowid
    conn.commit()
    conn.close()
    return application_id

def get_all_applications():
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT * FROM applications 
        ORDER BY submission_date DESC
    """)
    applications = c.fetchall()
    conn.close()
    return applications

# Quote functions
def save_quotes(application_id, quotes):
    conn = get_db()
    c = conn.cursor()
    
    for quote in quotes:
        c.execute("""
            INSERT INTO quotes 
            (application_id, carrier, plan_type, plan_name, network, monthly_premium, cost_per_period, generated_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            application_id,
            quote['carrier'],
            quote['type'],
            quote['plan_name'],
            quote['network'],
            float(quote['monthly_premium'].replace('$', '')),
            float(quote['cost_per_period'].replace('$', '')),
            datetime.datetime.now()
        ))
    
    conn.commit()
    conn.close()

def get_quotes_by_ref(quote_ref):
    conn = get_db()
    c = conn.cursor()
    
    c.execute("""
        SELECT q.* FROM quotes q
        JOIN applications a ON q.application_id = a.id
        WHERE a.quote_ref = ?
    """, (quote_ref,))
    
    quotes = c.fetchall()
    conn.close()
    return quotes 