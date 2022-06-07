import argparse
from module import load_modules, run_module
from custom_modules import shodan_client, securitytrails_client
from helper import sort_and_unique, remove_zero_size_files, get_env_vars
from banner import print_banner

parser = argparse.ArgumentParser('dprcn', description="A module-oriented swiss knife for recon")
parser.add_argument('-d', help="the domain url", required=True)
parser.add_argument('-o', help="directory where you want to save your output", required=True)
parser.add_argument('-v', help="verbose mode", required=False)

args = parser.parse_args()
env_vars = get_env_vars()

def init(domain, directory):
    print_banner()

    modules = load_modules(domain, directory)
    for module in modules:
        run_module(module)

    securitytrails_client.get_hosts(domain, directory, env_vars['SECURITY_TRAILS_API_KEY'])
    shodan_client.get_hosts(domain, directory, env_vars['SHODAN_API_KEY'])
   
    sort_and_unique(directory)
    remove_zero_size_files([f'{directory}/DNS'])

if __name__ == '__main__':
    init(args.d, args.o)
