import sqlite3
import os

# Ensure 'data' directory exists
if not os.path.exists("data"):
    os.makedirs("data")

# Connect to SQLite database
conn = sqlite3.connect("data/company.db")
cursor = conn.cursor()

# Create Employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Department TEXT,
    Salary INTEGER,
    Hire_Date TEXT
);
""")

# Create Departments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Departments (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT UNIQUE,
    Manager TEXT
);
""")

# Insert department data (Fixed issue with missing Engineering)
departments = [
    ('Sales', 'Alice'),
    ('Engineering', 'Bob'),
    ('Marketing', 'Charlie')
]
cursor.executemany("INSERT OR IGNORE INTO Departments (Name, Manager) VALUES (?, ?)", departments)

# Insert employee data (Fixed issue with missing Bob in Engineering)
employees = [
    ('Alice', 'Sales', 50000, '2021-01-15'),
    ('Bob', 'Engineering', 70000, '2020-06-10'),
    ('Charlie', 'Marketing', 60000, '2022-03-20')
]
cursor.executemany("INSERT OR IGNORE INTO Employees (Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?)", employees)

# Commit changes and close
conn.commit()
conn.close()

print("Database initialized with correct schema and data.")
