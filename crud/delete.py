import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

def delete_user(user_id):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query= '''DELETE FROM users WHERE id = %s'''
            cursor.execute(query,(user_id,))
            conn.commit()
            cursor.close()
            print(f'User {user_id} deleted successfully')
        except Exception as e:
            print(f'Error deleting user: {e}')
        finally:
            cursor.close()
            conn.close()


# delete_user(1)