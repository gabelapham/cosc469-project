import re
import requests
from pysafebrowsing import SafeBrowsing
from urllib.parse import urlparse
from collections import Counter

def check_url(url):
    if "http://" in url or "https://" in url:
        return is_phishing_url(url)
    else:
        return is_phishing_url(f"http://{url}")

def is_phishing_url(url):
    safeBrowse = SafeBrowsing("AIzaSyCn-O7mE1Cgv5Nwxx7GbuO9PMSJc3UWM6Q") # Google Safe Browsing API Key
    result = safeBrowse.lookup_urls([url])
    if result and result[url]["malicious"]:
        return True

    parsed_url = urlparse(url)

    suspicious_domains = ["phishing", "hack", "malicious", "reward", "deal", "@"]
    for domain in suspicious_domains:
        if domain in parsed_url.netloc:
            return True
    
    countUrl = Counter(url)
    if countUrl["."] > 2:
        return True
    countNetloc = Counter(parsed_url.netloc)
    if countNetloc["-"] > 2:
        return True

    suspicious_keywords = ["login", "password", "account", "verify", "reward", "deal", "@", "-", "."]
    for keyword in suspicious_keywords:
        if keyword in parsed_url.path:
            return True

    ip_pattern = re.compile(
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    )
    if ip_pattern.match(parsed_url.netloc):
        return True

    if len(url) > 100:
        return True

    return False

if __name__ == "__main__":
    url = input("Enter a URL to check: ")
    result = check_url(url)
    if result:
        print("This URL is potentially a phishing site.")
    else:
        print("This URL appears to be safe.")

