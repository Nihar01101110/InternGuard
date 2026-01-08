from preProcessing import url
import re
from urllib.parse import urlparse
#URL=url
URL="https://chatgpt.com/c/695fc5b3-dd3c-8327-9d59-4793e492f977"

SUSPICIOUS_TLDS = [
    ".xyz", ".tk", ".ml", ".ga", ".cf", ".gq", ".top", ".zip"
]

BRAND_DOMAINS = {
    "google": ["google.com"],
    "amazon": ["amazon.com", "amazon.in"],
    "microsoft": ["microsoft.com"],
    "facebook": ["facebook.com"],
    "instagram": ["instagram.com"]
}

CAREER_KEYWORDS = [
    "internship", "career", "job", "hiring", "apply", "placement"
]


def normalize_url(url):
    return url.strip().lower()


def extract_url_parts(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    scheme = parsed.scheme
    return scheme, domain


def is_ip_address(domain):
    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    return re.match(ip_pattern, domain) is not None



def check_https(scheme, signals):
    risk = 0
    if scheme != "https":
        risk += 20
        signals.append("Uses HTTP instead of HTTPS")
    return risk


def check_suspicious_tld(domain, signals):
    risk = 0
    for tld in SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            risk += 25
            signals.append(f"Suspicious TLD detected ({tld})")
            break
    return risk


def check_brand_impersonation(domain, signals):
    risk = 0
    for brand, official_domains in BRAND_DOMAINS.items():
        if brand in domain:
            if not any(domain.endswith(official) for official in official_domains):
                risk += 30
                signals.append(f"Possible brand impersonation ({brand})")
    return risk


def check_hyphens(domain, signals):
    risk = 0
    hyphen_count = domain.count("-")
    if hyphen_count >= 2:
        risk += 10
        signals.append("Multiple hyphens found in domain")
    return risk


def check_keywords(url, signals):
    risk = 0
    for keyword in CAREER_KEYWORDS:
        if keyword in url:
            risk += 15
            signals.append(f"Suspicious keyword detected ({keyword})")
            break
    return risk


def check_url_length(url, signals):
    risk = 0
    if len(url) > 75:
        risk += 10
        signals.append("URL length is unusually long")
    return risk


def check_ip_usage(domain, signals):
    risk = 0
    if is_ip_address(domain):
        risk += 25
        signals.append("IP address used instead of domain name")
    return risk



def analyze_url(url):
    url = normalize_url(url)
    scheme, domain = extract_url_parts(url)

    risk_score = 0
    signals = []

    risk_score += check_https(scheme, signals)
    risk_score += check_suspicious_tld(domain, signals)
    risk_score += check_brand_impersonation(domain, signals)
    risk_score += check_hyphens(domain, signals)
    risk_score += check_keywords(url, signals)
    risk_score += check_url_length(url, signals)
    risk_score += check_ip_usage(domain, signals)


    return risk_score
a=analyze_url(URL)#store the url and variable is a
#if the value of "a" is more than 20 or 25 then danger and if the value of the a ir more than 50 then very dangerous