import os
import sys
import logging
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
dl_dir = os.path.join(base_dir, '../tmp/downloads/')

def setup_logger():
    current_datetime = datetime.now().strftime('%m-%d-%y_%H-%M-%S')
    log_filename = f"download_{current_datetime}-summary.log"
    log_path = os.path.join(f'{base_dir}/../tmp/logs', log_filename)
    
    logger = logging.getLogger('Scraper')
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(log_path)
    console_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger