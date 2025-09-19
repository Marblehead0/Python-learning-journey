import logging
from pathlib import Path

LOG = Path(__file__).with_name("app.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG, encoding="utf-8"), logging.StreamHandler()]
)

def divide(a,b):
    logging.debug("divide called with a=%s",a,b)
    try:
        res = a / b
        logging.info("Success: %s / %s = %s",a,b,res)
        return res
    except ZeroDivisionError:
        logging.exception("Divsion by zero")
        return None
    
if __name__ == "__main__":
    logging._Level = logging.debug
    divide(10,2)
    divide(5,0)
