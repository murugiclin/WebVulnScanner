import argparse
import json
from src.scanner.xss import XSSScanner
from src.scanner.headers import HeaderScanner
from src.scanner.sql_injection import SQLInjectionScanner
from src.utils.logger import setup_logger
from src.report.reporter import ReportGenerator

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="WebVulnScanner: A modular web vulnerability scanner")
    parser.add_argument("url", help="Target URL to scan (e.g., http://example.com)")
    parser.add_argument("--output", default="report.json", help="Output file for scan report")
    args = parser.parse_args()

    # Initialize logger
    logger = setup_logger()

    # Ethical use disclaimer
    logger.info("WebVulnScanner: For educational purposes only. Ensure you have permission to scan the target.")
    
    # Initialize scanners
    xss_scanner = XSSScanner(args.url)
    header_scanner = HeaderScanner(args.url)
    sql_scanner = SQLInjectionScanner(args.url)
    
    # Perform scans
    logger.info(f"Starting scan on {args.url}")
    results = {
        "url": args.url,
        "xss_vulnerabilities": xss_scanner.scan(),
        "header_issues": header_scanner.scan(),
        "sql_injection_indicators": sql_scanner.scan()
    }
    
    # Generate report
    reporter = ReportGenerator(results)
    reporter.save_report(args.output)
    logger.info(f"Scan completed. Report saved to {args.output}")

if __name__ == "__main__":
    main()
