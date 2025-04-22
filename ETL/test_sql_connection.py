import os
import sys

# Add the DOMi root folder to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from Config.settings_loader import SQL_SERVER, SQL_DATABASE
import pyodbc

def test_connection():
    try:
        conn_str = (
            f"DRIVER={{SQL Server}};"
            f"SERVER={SQL_SERVER};"
            f"DATABASE={SQL_DATABASE};"
            f"Trusted_Connection=yes;"
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT TOP 5 name FROM sys.tables")
        rows = cursor.fetchall()

        print("✅ Connection successful. Tables in database:")
        for row in rows:
            print("-", row.name)
        conn.close()

    except Exception as e:
        print("❌ Connection failed:", e)

if __name__ == "__main__":
    test_connection()
