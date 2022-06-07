from genericpath import isfile
from os import system, listdir, stat, remove, getcwd
from os.path import isfile, join

def write_to_file(filename, content):
    """ Writes the desired content to a file of choice"""
    try:
        f = open(filename, 'w', encoding = 'utf-8')
        list(map(lambda line: f.write(f"{line}\n"), content))
    except Exception as err:
        print(f"write_to_file(): Couldn't write to file {filename} ", err)
    finally:
        f.close()

def remove_zero_size_files(directories = []):
    """ Remove files with 0 size from the directories 
    Returns 'True' if the operation exits successfully 
    Returns 'False' if the operation exits with error 
    """
    try:
        for directory in directories:
            only_files = [f for f in listdir(directory) if isfile(join(directory, f))]
            for file in only_files:
                normalizeds_file = f'{directory}/{file}'
                if stat(normalizeds_file).st_size == 0:
                    remove(f'{normalizeds_file}')
            return True
    
    except Exception as err:
        print('Error files_cleanup():', err)

    return False

def sort_and_unique(directory):
    """ Sort and remove duplicates files with 0 size
    Returns 'True' if the operation exits successfully 
    Returns 'False' if the operation exits with error 
    """
    return system(f'cat {directory}/domains/*.subdomains | sort -u >> {directory}/assets.txt') == 0

def get_env_vars():
    """ 
    Read environemtn variables defined at .env file.
    """
    env_vars = {}
    with open(f'{getcwd()}/.env') as f:
        for line in f.readlines():
            key_value = line.strip().split("=")
            env_vars[key_value[0]] = key_value[1]

    return env_vars

