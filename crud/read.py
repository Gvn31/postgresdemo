import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

def get_user(user_id):
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            cursor.close()
            if user:
                print(f'User found: {user}')
            else:
                print(f'No user found with ID: {user_id}')

        except Exception as e:
            print(f"Error reading user: {e}")
        finally:
            cursor.close()
            conn.close()


# get_user(1)