import requests
from src.utils.logger import get_logger
from src.utils.request_handler import make_request

class HeaderScanner:
    def __init__(self, url):
        self.url = url
        self.logger = get_logger()
        self.required_headers = ["Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options"]
    
    def scan(self):
        self.logger.info(f"Scanning {self.url} for insecure headers")
        try:
            response = make_request(self.url)
            headers = response.headers
            issues = []
            
            for header in self.required_headers:
                if header not in headers:
                    issues.append(f"Missing header: {header}")
                elif header == "X-Frame-Options" and headers[header].lower() not in ["deny", "sameorigin"]:
                    issues.append(f"Insecure {header}: {headers[header]}")
            return issues
        except Exception as e:
            self.logger.error(f"Error scanning {self.url} for headers: {e}")
            return []
