# Basic Web Vulnerability Scanner

A simple Python script to scan websites for basic security vulnerabilities such as:
- Missing security headers
- Open directories
- Insecure HTTP methods
- Basic SQL Injection

##  Aim

To understand and implement a basic web vulnerability scanner using Python and HTTP requests.

##  Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

## Install with:

bash
pip install -r requirements.txt

## Usage:
bash
python scanner.py

Then enter a target URL like:
https://testphp.vulnweb.com/artists.php?artist=1

## Features:

Checks for missing HTTP security headers

Detects open directory listings

Lists risky HTTP methods (e.g., PUT, DELETE)

Scans for basic SQL injection payloads

## OUTPUT:

<img width="1562" height="1079" alt="Screenshot 2025-08-04 231225" src="https://github.com/user-attachments/assets/c1304700-f513-4145-b0ce-223f0c696171" />

[✓] Connected to https://example.com (Status: 200)

[+] Checking HTTP Headers...
⚠️ Missing security header: X-Frame-Options

[+] Checking for open directory listing...
❌ Directory listing not detected.

[+] Checking Allowed HTTP Methods (OPTIONS)...
✅ Allowed Methods: GET, POST, PUT
⚠️ Risky method enabled: PUT

[+] Checking for basic SQL Injection vulnerabilities...
⚠️ Possible SQL Injection with payload: ' OR '1'='1


