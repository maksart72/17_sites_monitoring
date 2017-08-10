import sys
import re
import os


def load_urls4check(path):
    with open(filepath, 'r') as file:
        return file.read()

def validate_urls(url):
    pass

def is_server_respond_with_200(url):
    pass
    return True

def get_domain_expiration_date(domain_name):
    pass
    return True

def print_domain_status(domain_info)
    for url in urls_list:
        print('Site: %s Active: %s Expired: %s'%(url,is_server_respond_with_200(url),get_domain_expiration_date(url)))
    
if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print("Error: Empty argument, try check_sites_health.py <filename>")
        exit()
    filename = sys.argv[1]
    if (bool(filename)) and (os.path.isfile(filename)):
        urls_list = load_urls4check(filename)
        is_server_respond_with_200(url)
        get_domain_expiration_date(domain_name)






    else:
        print("Error! File doesn't exist!")
