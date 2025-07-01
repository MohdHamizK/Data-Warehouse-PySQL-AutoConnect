from etl_sales import insert_sample_sale  # ✅ Added import
from date_utils import ensure_dim_date_populated
import psycopg2
import psycopg2
from date_utils import ensure_dim_date_populated

def run_etl():
    conn = psycopg2.connect(
        dbname="Project",
        user="postgres",
        password="Hamiz@sql",
        host="localhost",
        port="5432"
    )

    print("🔄 Validating dim_date...")
    ensure_dim_date_populated(conn)

    print("📦 Inserting sample sales...")
    insert_sample_sale(conn)

    conn.close()
    print("✅ ETL completed successfully")

if __name__ == "__main__":
    run_etl()