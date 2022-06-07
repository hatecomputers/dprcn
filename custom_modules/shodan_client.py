import shodan
import os
from json import loads, dumps

SHODAN_API_KEY = os.environ['SHODAN_API_KEY']

api = shodan.Shodan(SHODAN_API_KEY)

def flatten(t):
    return [item for sublist in t for item in sublist]

def get_hosts(domain, directory):
    return get_data(f'hostname:"{domain}"', directory)

def get_data(query, directory):
       
    try:
        results = api.search(query)
        hostnames = list(map(lambda match: match['hostnames'], results['matches']))
        
        fw = open(f'{directory}/domains/shodan.subdomains', 'a+')
        
        for hostname in set(flatten(hostnames)):
            fw.write(f'{hostname}\n')

    except shodan.APIError as e:
        print('Error: {}'.format(e))
