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
    request = requests.get(url)
    return request.status_code


def get_domain_expiration_date(url):
    whois_data = whois.whois(url)
    whois_expiration = whois_data.expiration_date
    if type(whois_expiration) is list:
        expiration_date = whois_expiration[0]
    else: 
        expiration_date = whois_expiration
    return expiration_date

def print_domain_status(url):
    print('URL:%s | Status:%s | Expired in:%s '%
          (url, is_server_respond_with_200(url), get_domain_expiration_date(url) - datetime.datetime.now()))


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print("Error: Empty argument, try check_sites_health.py <filename>")
        exit()
    filename = sys.argv[1]
    if (bool(filename)) and (os.path.isfile(filename)):
        urls4check = load_urls4check(filename)
        for url in urls4check:
            print_domain_status(url)
    else:
        print("Error! File doesn't exist!")
