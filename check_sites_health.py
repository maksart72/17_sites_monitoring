import sys
import re
import os
import requests


def load_urls4check(filepath):
    with open(filepath, 'r') as file:
        url_list = [(url.strip()).lower() for url in file]
   print(url_list)

def validate_urls(urls):
    url_list = []
    for url in urls:
        url_list.append(url)
    print(url_list)

def is_server_respond_with_200(url):
        request = requests.get(url)
        print(request.status_code)

def get_domain_expiration_date(url):
    print('not expired')

def print_domain_status(url):
    print('Site: %s Active: %s Expired: %s'%(url,is_server_respond_with_200(url),get_domain_expiration_date(url)))

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print("Error: Empty argument, try check_sites_health.py <filename>")
        exit()
    filename = sys.argv[1]
    if (bool(filename)) and (os.path.isfile(filename)):
        urls4check = load_urls4check(filename)
        url_list = validate_urls(urls4check)
        for url in url_list:
            print_domain_status(url)
    else:
        print("Error! File doesn't exist!")

'''
  
        request = requests.get(url)
        ConnectionError('Error') 
        print(request.status_code)

def get_domain_expiration_date(domain_name):
    pass
    return True

def print_domain_status(domain_info):
    for url in urls_list:
        
    

    is_server_respond_with_200('http://ytttttta.ru')

    
    
    
        urls_list = load_urls4check(filename)
        is_server_respond_with_200(url)
        get_domain_expiration_date(domain_name)

'''