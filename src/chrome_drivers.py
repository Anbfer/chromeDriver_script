import request_get as r
import find_chrome_version as fcv
import re
from bs4 import BeautifulSoup

def driver_versions():
    
    drivers_versions = r.get_uri_no_strip("https://chromedriver.storage.googleapis.com/")

    soup = BeautifulSoup(drivers_versions, 'xml')

    versions = set()
    for key in soup.find_all('Key'):
        if key:
            match = re.match(r'^(\d+\.\d+\.\d+\.\d+)/', key.text)
            if match:
                versions.add(match.group(1))
    sorted_versions = sorted(versions)
    
    return sorted_versions