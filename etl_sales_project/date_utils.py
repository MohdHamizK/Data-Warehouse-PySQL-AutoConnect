# date_utils.py

import psycopg2
from datetime import datetime, timedelta

def ensure_dim_date_populated(conn, start_date='2020-01-01', end_date='2030-12-31'):
    """
    Ensures dim_date contains all dates between start_date and end_date
    """
    try:
        cur = conn.cursor()

        # Generate all dates between start and end
        current = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')

        while current <= end:
            current_date_str = current.strftime('%Y-%m-%d')
            cur.execute("""
                INSERT INTO dim_date (full_date, day_of_week, day_num_in_month, day_name, month_num, month_name, year)
                SELECT %s, EXTRACT(DOW FROM %s::DATE)::INT, EXTRACT(DAY FROM %s::DATE)::INT,
                       TO_CHAR(%s::DATE, 'Day'), EXTRACT(MONTH FROM %s::DATE)::INT,
                       TO_CHAR(%s::DATE, 'Month'), EXTRACT(YEAR FROM %s::DATE)::INT
                WHERE NOT EXISTS (
                    SELECT 1 FROM dim_date WHERE full_date = %s::DATE
                )
            """, (current_date_str,) * 8)

            current += timedelta(days=1)

        conn.commit()
        cur.close()
        print("✅ dim_date validated and updated")
    except Exception as e:
        print(f"❌ Error updating dim_date: {e}")
        conn.rollback()