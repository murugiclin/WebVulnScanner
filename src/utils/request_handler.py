import requests
from src.utils.logger import get_logger

def make_request(url, timeout=5):
    logger = get_logger()
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        logger.error(f"Request to {url} failed: {e}")
        raise
