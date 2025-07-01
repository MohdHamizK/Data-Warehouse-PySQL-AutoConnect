# sales_dw_utils/logger.py
import logging
import os
from datetime import datetime

LOG_FILE = f"email_sender_{datetime.now().strftime('%Y%m%d')}.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def get_logger():
    return logging.getLogger(__name__)