import re
import math
from urllib.parse import urlparse
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
SUSPICIOUS_DOMAIN_WORDS=[
    "offer","fast","free","instant","win","gurantee"
]


WEIGHTS = {
    "http": 1.2,
    "tld": 1.8,
    "brand": 2.5,
    "hyphen": 0.8,
    "keyword": 2.0,
    "length": 0.6,
    "ip": 2.0
    "suspicious_word":2.0
}

def is_ip_address(domain):
    pattern = r"\d{1,3}(\.\d{1,3}){3}"
    return re.fullmatch(pattern, domain) is not None

def extract_features(url):
    parsed_url = urlparse(url.lower())
    domain = parsed_url.netloc

    features = {}

  
    if parsed_url.scheme == "https":
        features["http"] = 0.3
    else:
        features["http"] = 1

 
    features["tld"] = 0
    for tld in SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            features["tld"] = 1
            break

    
    features["brand"] = 0

    for brand in BRAND_DOMAINS:
        if brand in domain:
            valid_domains = BRAND_DOMAINS[brand]

            is_legit = False
            for legit_domain in valid_domains:
                if domain.endswith(legit_domain):
                    is_legit = True
                    break

            if is_legit == False:
                features["brand"] = 1
                break

  
    hyphen_count = domain.count("-")

    if hyphen_count >= 2:
        features["hyphen"] = 1
    else:
        features["hyphen"] = hyphen_count / 2


    features["keyword"] = 0
    for word in CAREER_KEYWORDS:
        if word in url:
            features["keyword"] = 1
            break

    
    url_length = len(url)

    if url_length >= 100:
        features["length"] = 1
    else:
        features["length"] = url_length / 100

   
    if is_ip_address(domain):
        features["ip"] = 1
    else:
        features["ip"] = 0

    features["suspicious_word"] = 0
    for word in SUSPICIOUS_DOMAIN_WORDS:
        if word in domain:
            features["suspicious_word"] = 1
            break

    return features




def calculate_probability(features):
    score = 0

    for feature in features:
        score += features[feature] * WEIGHTS[feature]

    
    probability = 1 / (1 + math.exp(-score))
    return probability



def analyze_url(url):
    features = extract_features(url)
    probability = calculate_probability(features)

    
    risk_percentage = round(probability * 100, 2)
    return risk_percentage
