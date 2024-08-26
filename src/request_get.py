import requests

def get_uri_strip(uri):
    return requests.get(uri).text.strip()

def get_uri_no_strip(uri):
    return requests.get(uri).text