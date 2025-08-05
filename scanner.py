import requests
from bs4 import BeautifulSoup

url = input("Enter the website URL (e.g., https://example.com): ")

# Check HTTP headers
def check_headers(response):
    print("\n[+] Checking HTTP Security Headers:")
    headers = {
        'Content-Security-Policy': 'Content Security Policy',
        'X-Content-Type-Options': 'MIME Sniffing Protection',
        'X-Frame-Options': 'Clickjacking Protection',
        'Strict-Transport-Security': 'HTTPS Enforcement',
        'X-XSS-Protection': 'Cross-site Scripting Protection'
    }
    for header in headers:
        if header in response.headers:
            print(f" {headers[header]} is enabled.")
        else:
            print(f"{headers[header]} is MISSING!")

# Check for open directories
def check_open_directory():
    print("\n[+] Checking for Open Directories...")
    paths = ["/admin", "/backup", "/test", "/old", "/login", "/uploads"]
    for path in paths:
        test_url = url.rstrip("/") + path
        res = requests.get(test_url)
        if res.status_code == 200 and "Index of /" in res.text:
            print(f" Open directory found at: {test_url}")
        elif res.status_code == 200:
            print(f"Accessible: {test_url}")
        else:
            print(f" Not found: {test_url}")
def check_http_methods():
    print("\n[+] Checking Allowed HTTP Methods (OPTIONS)...")
    try:
        options_response = requests.options(url)
        methods = options_response.headers.get('Allow')
        if methods:
            print(f" Allowed Methods: {methods}")
            risky_methods = ['PUT', 'DELETE', 'TRACE', 'CONNECT']
            for method in risky_methods:
                if method in methods:
                    print(f"Risky method enabled: {method}")
        else:
            print(" Could not determine allowed methods.")
    except Exception as e:
        print(f" Error checking HTTP methods: {e}")

def check_sql_injection():
    print("\n[+] Checking for basic SQL Injection vulnerabilities...")
    test_payloads = ["'", "' OR '1'='1", '" OR "1"="1', "';--", '" OR 1=1--']
    
    if '?' not in url:
        print(" No parameters in URL to test for SQL Injection.")
        return
    
    for payload in test_payloads:
        injected_url = url.split('?')[0] + '?'
        params = url.split('?')[1].split('&')
        
        new_params = []
        for param in params:
            key = param.split('=')[0]
            new_params.append(f"{key}={payload}")
        
        test_url = injected_url + '&'.join(new_params)
        try:
            r = requests.get(test_url)
            if any(error in r.text.lower() for error in ['sql', 'syntax', 'mysql', 'warning']):
                print(f" Possible SQL Injection vulnerability with payload: {payload}")
                print(f"   → URL: {test_url}")
        except Exception as e:
            print(f"Error testing payload {payload}: {e}")


# Main
try:
    response = requests.get(url)
    print(f"\n[✓] Connected to {url} (Status: {response.status_code})")
    check_headers(response)
    check_open_directory()
    check_http_methods()
    check_sql_injection()  # <-- Add this line
except Exception as e:
    print(f"\n[✖] Could not connect to {url}: {e}")


