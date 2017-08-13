import sys
import os
import requests
import validators
import whois
import datetime


def load_urls4check(filepath):
    with open(filepath, 'r') as file:
        url_list = [(url.strip()).lower()
                    for url in file if validators.url(url)]
    return url_list

def is_server_respond_with_200(url):
    try:
        request = requests.get(url)
        status_code = request.status_code
    except requests.exceptions.RequestException:
        status_code = None
    return status_code

def get_domain_expiration_date(url):
    if is_server_respond_with_200(url) is None:
        expiration_date = None
    else:    
        whois_data = whois.whois(url)
        whois_expiration = whois_data.expiration_date
        if type(whois_expiration) is list:
            expiration_date = whois_expiration[0] - datetime.datetime.now()
        else:
            expiration_date = whois_expiration - datetime.datetime.now()
    return expiration_date

def print_domain_status(url):
    print('URL:%s | Status:%s | Expired in:%s '%(url, is_server_respond_with_200(url), get_domain_expiration_date(url)))


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print("Error: Empty argument, try check_sites_health.py <filename>")
        exit()
    filename = sys.argv[1]
    if (bool(filename)) and (os.path.isfile(filename)):
        urls4check = load_urls4check(filename)
        if len(urls4check) >= 1:
            for url in urls4check:
                print_domain_status(url)
        else:
            print('Error: File doesn\'t contains correct URL')
    else:
        print("Error: File doesn't exist!")
