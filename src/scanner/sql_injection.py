from bs4 import BeautifulSoup
from src.utils.logger import get_logger
from src.utils.request_handler import make_request

class SQLInjectionScanner:
    def __init__(self, url):
        self.url = url
        self.logger = get_logger()
    
    def scan(self):
        self.logger.info(f"Scanning {self.url} for SQL injection indicators")
        try:
            response = make_request(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')
            indicators = []
            
            for form in forms:
                if form.get('method', '').lower() == 'get':
                    indicators.append({
                        "form_action": form.get('action', ''),
                        "issue": "GET method used, potentially vulnerable to SQL injection"
                    })
            return indicators
        except Exception as e:
            self.logger.error(f"Error scanning {self.url} for SQL injection: {e}")
            return []
