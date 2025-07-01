import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
from .config import EMAIL_CONFIG
from .logger import get_logger
from datetime import datetime
from .db_utils import run_query
import csv
import os

logger = get_logger()

EMAIL_TEMPLATE = """
<html>
  <body>
    <h2>🚀 Daily Sales & MV Refresh Report</h2>
    <p><strong>Status:</strong> ✅ Success</p>
    <p><strong>Timestamp:</strong> {timestamp}</p>

    <h3>📅 Today's Sales Summary</h3>
    <table border="1" cellpadding="8">
      <tr><th>Date</th><th>Total Orders</th><th>Total Sales</th></tr>
      <tr><td>{date}</td><td>{orders}</td><td>${sales:,.2f}</td></tr>
    </table>

    <hr>
    <p>Sent from: Sales Data Warehouse Automation</p>
  </body>
</html>
"""

def generate_daily_sales_csv():
    data = run_query("""
        SELECT 
            d.full_date,
            COUNT(*) AS total_orders,
            SUM(s.net_amount) AS total_sales
        FROM fact_sales s
        JOIN dim_date d ON s.date_key = d.date_key
        WHERE d.full_date = CURRENT_DATE
        GROUP BY d.full_date;
    """)
    if not data:
        return None

    filename = f"daily_sales_{datetime.now().strftime('%Y%m%d')}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Total Orders', 'Total Sales'])
        writer.writerows(data)
    return filename

def send_daily_sales_email():
    daily_data = run_query("""
        SELECT 
            d.full_date,
            COUNT(*) AS total_orders,
            SUM(s.net_amount) AS total_sales
        FROM fact_sales s
        JOIN dim_date d ON s.date_key = d.date_key
        WHERE d.full_date = CURRENT_DATE
        GROUP BY d.full_date;
    """)

    if daily_data:
        date, orders, sales = daily_data[0]
    else:
        date, orders, sales = "N/A", 0, 0.0

    html_content = EMAIL_TEMPLATE.format(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        date=date,
        orders=orders,
        sales=sales
    )

    msg = EmailMessage()
    msg['Subject'] = "📊 Daily Sales & MV Refresh Report"
    msg['From'] = EMAIL_CONFIG['sender']
    msg['To'] = EMAIL_CONFIG['receiver']
    cid = make_msgid()
    msg.add_alternative(html_content, subtype='html')

    attachment_path = generate_daily_sales_csv()
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, 'rb') as f:
            file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=os.path.basename(attachment_path))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_CONFIG['sender'], EMAIL_CONFIG['password'])
            server.send_message(msg)
        logger.info("✅ Email sent successfully!")
    except Exception as e:
        logger.error(f"❌ Failed to send email: {e}")