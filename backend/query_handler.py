from backend.database import get_db_connection  # Use absolute import

def handle_query(user_input: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query: "Show me all employees in [department]"
    if user_input.lower().startswith("show me all employees in"):
        department = user_input.split("in")[-1].strip()
        cursor.execute("SELECT Name FROM Employees WHERE Department = ?", (department,))
        employees = cursor.fetchall()
        conn.close()
        return [emp["Name"] for emp in employees] if employees else "No employees found in this department."

    # Query: "Who is the manager of [department]?"
    elif user_input.lower().startswith("who is the manager of"):
        department = user_input.split("of")[-1].strip()
        cursor.execute("SELECT Manager FROM Departments WHERE Name = ?", (department,))
        manager = cursor.fetchone()
        conn.close()
        return manager["Manager"] if manager else "Department not found."

    # Query: "List all employees hired after [date]"
    elif user_input.lower().startswith("list all employees hired after"):
        date = user_input.split("after")[-1].strip()
        cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
        employees = cursor.fetchall()
        conn.close()
        return [emp["Name"] for emp in employees] if employees else "No employees found hired after this date."

    # Query: "What is the total salary expense for [department]?"
    elif user_input.lower().startswith("what is the total salary expense for"):
        department = user_input.split("for")[-1].strip()
        cursor.execute("SELECT SUM(Salary) AS Total FROM Employees WHERE Department = ?", (department,))
        total_salary = cursor.fetchone()
        conn.close()
        return f"Total salary expense: {total_salary['Total']}" if total_salary and total_salary["Total"] else "No data available for this department."

    else:
        conn.close()
        return "Sorry, I don't understand that query."
