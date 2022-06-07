import requests;
import os;
from json import loads, JSONDecodeError;
import logging;
from helper import write_to_file;

def parse_response(domain, encoded_json):
    try:
        parsed_json = loads(encoded_json)
        return list(map(lambda subdomain: f'{subdomain}{domain}', parsed_json['subdomains']))

    except JSONDecodeError as error:
        print('parsed_security_trails_data(): Error while decoding JSON ', error)

def get_url(domain = ''): 
    return f'https://api.securitytrails.com/v1/domain/{domain}/subdomains?children_only=true'


def get_hosts(domain, directory):
    headers = {
        'apiKey': os.environ['SECURITY_TRAILS_API_KEY'] 
    }
    
    try:
        response = requests.get(
            get_url(domain), headers=headers
        )
        
        if response.status_code == 200:
           write_to_file(f'{directory}/domains/security-trails.subdomains', parse_response(domain, response.text))
          
    except Exception as err:
        logging.error('Something went wrong.', err)
