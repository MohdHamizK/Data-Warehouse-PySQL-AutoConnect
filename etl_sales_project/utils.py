# utils.py

import psycopg2
from datetime import date

def get_current_date_key(conn):
    """
    Fetches today's date_key from dim_date
    """
    try:
        cur = conn.cursor()
        today = date.today().strftime('%Y-%m-%d')
        cur.execute("SELECT date_key FROM dim_date WHERE full_date = %s", (today,))
        result = cur.fetchone()
        cur.close()
        if result:
            return result[0]
        else:
            raise ValueError(f"No date_key found for {today}")
    except Exception as e:
        print(f"Error getting date_key: {e}")
        return None