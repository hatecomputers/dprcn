from runpy import run_module
import argparse
from module import load_modules, run_module
from custom_modules import shodan_client, securitytrails_client
from helper import sort_and_unique, remove_zero_size_files
import sys;

parser = argparse.ArgumentParser('dope-recon', description="a module oriented recon swiss knife")
parser.add_argument('-d', help="the domain url", required=True)
parser.add_argument('-o', help="directory where you want to save your output", required=True)

args = parser.parse_args()

def init(domain, directory):
    modules = load_modules(domain, directory)
    for module in modules:
        run_module(module)

    securitytrails_client.get_hosts(domain, directory)
    shodan_client.get_hosts(domain, directory)
   
    sort_and_unique(directory)
    remove_zero_size_files([f'{directory}/DNS'])

if __name__ == '__main__':
    init(args.d, args.o)
