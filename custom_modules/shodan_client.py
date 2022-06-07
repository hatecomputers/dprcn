import shodan

def flatten(t):
    return [item for sublist in t for item in sublist]

def get_hostnames(matches):
    return list(map(lambda match: match['hostnames'], matches))

def get_hosts(domain, directory):
    return get_data(f'hostname:"{domain}"', directory)

def get_data(query, directory, api_key):
    api = shodan.Shodan(api_key)

    try:
        results = api.search(query)
        hostnames = get_hostnames(results['matches'])
    
        fw = open(f'{directory}/domains/shodan.subdomains', 'a+')
        
        for hostname in set(flatten(hostnames)):
            fw.write(f'{hostname}\n')

    except shodan.APIError as e:
        print('Error: {}'.format(e))
