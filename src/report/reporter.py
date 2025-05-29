import json
from src.utils.logger import get_logger

class ReportGenerator:
    def __init__(self, results):
        self.results = results
        self.logger = get_logger()
    
    def save_report(self, output_file):
        try:
            with open(output_file, 'w') as f:
                json.dump(self.results, f, indent=4)
            self.logger.info(f"Report saved to {output_file}")
        except Exception as e:
            self.logger.error(f"Error saving report: {e}")
