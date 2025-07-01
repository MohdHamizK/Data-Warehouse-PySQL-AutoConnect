# etl_sales.py

import psycopg2
from utils import get_current_date_key

def insert_sample_sale(conn):
    """
    Inserts a sample sale record using today's date_key
    """
    try:
        cur = conn.cursor()
        current_date_key = get_current_date_key(conn)
        if not current_date_key:
            raise Exception("Could not retrieve date_key")

        # Sample sale data
        order_id = "ORD-999"
        customer_id = 1
        product_id = 1
        store_id = 1
        quantity_sold = 2
        unit_price = 19.99
        total_amount = 39.98
        discount_amount = 5.00
        net_amount = 34.98

        cur.execute("""
            INSERT INTO fact_sales (
                order_id, customer_id, product_id, store_id, date_key,
                quantity_sold, unit_price, total_amount, discount_amount, net_amount
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            order_id, customer_id, product_id, store_id, current_date_key,
            quantity_sold, unit_price, total_amount, discount_amount, net_amount
        ))

        conn.commit()
        cur.close()
        print("✅ Sale inserted successfully")
    except Exception as e:
        print(f"❌ Error inserting sale: {e}")
        conn.rollback()