import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

def create_user(user_id,name):
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query='''INSERT INTO users(id,name) VALUES(%s,%s)'''
            cursor.execute(query,(user_id,name))
            conn.commit()
            cursor.close()
            print(f'User {name} created successfully')
        except Exception as e:
            print(f'Error creating user: {e}')
        finally:
            cursor.close()
            conn.close()

# create_user(1,'Jikku')