import requests
from bs4 import BeautifulSoup
from src.utils.logger import get_logger
from src.utils.request_handler import make_request

class XSSScanner:
    def __init__(self, url):
        self.url = url
        self.logger = get_logger()
        self.payloads = ["<script>alert('test')</script>", "<img src=x onerror=alert('test')>"]
    
    def scan(self):
        self.logger.info(f"Scanning {self.url} for XSS vulnerabilities")
        try:
            response = make_request(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')
            vulnerabilities = []
            
            for form in forms:
                action = form.get('action', '')
                method = form.get('method', 'get').lower()
                inputs = form.find_all('input')
                for input_tag in inputs:
                    if input_tag.get('type') in ['text', 'search']:
                        # Simulate payload injection (for demo purposes, log potential issues)
                        vulnerabilities.append({
                            "form_action": action,
                            "method": method,
                            "input_name": input_tag.get('name', 'unknown'),
                            "potential_xss": "Unfiltered input detected"
                        })
            return vulnerabilities
        except Exception as e:
            self.logger.error(f"Error scanning {self.url} for XSS: {e}")
            return []
