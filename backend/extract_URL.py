import re

def extract_url_and_text(text):
    url_pattern = r"https?://[^\s]+"
    match = re.search(url_pattern, text)
    url = match.group() if match else ""
    text_without_url = re.sub(url_pattern, "", text).strip()

    return url, text_without_url
#a file bas url separate karuchi
