# sales_dw_utils/db_utils.py
import psycopg2
from .config import DB_CONFIG
from .logger import get_logger

logger = get_logger()

def run_query(query):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        conn.close()
        logger.info("✅ Query executed successfully.")
        return result
    except Exception as e:
        logger.error(f"❌ Failed to execute query: {e}")
        return None

def refresh_materialized_view():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("REFRESH MATERIALIZED VIEW my_daily_sales;")
        conn.commit()
        logger.info("✅ Materialized view refreshed successfully.")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to refresh materialized view: {e}")
        return False
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()