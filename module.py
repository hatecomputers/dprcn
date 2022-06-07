from json import loads
from os import system
from constants import MODULE_FILEPATH, MODULE_INSTRUCTIION_ATTR, MODULE_SHOULD_RUN_ATTR
import colors

def load_modules(domain, directory):
    try: 
        f = open(MODULE_FILEPATH) 
        modules = loads(f.read());
        return normalize_nodules(domain, directory, modules).values()    
        
    except Exception as err:
        print(f'{colors.FAIL}Error - load_modules():{colors.ENDC}', err)
    finally:
        f.close()

def normalize_nodules(domain, directory, modules):
    for module_key in modules:
            current_modules = modules[module_key]['modules']
            for current_module in current_modules:
                  normalize_should_run =  True if current_module[MODULE_SHOULD_RUN_ATTR] == "True" else False
                  normalize_instruction = current_module[MODULE_INSTRUCTIION_ATTR].replace('{domain}', domain).replace('{directory}', directory)  

                  current_module[MODULE_SHOULD_RUN_ATTR] = normalize_should_run
                  current_module[MODULE_INSTRUCTIION_ATTR] = normalize_instruction
    
    return modules

def run_module(module):
    if module == None:
        return
    elif 'modules' in module:
        run_module(module['modules'])
    elif isinstance(module, list):
        for current_module in module:
            if current_module['should_run'] == True:
                print(f'{colors.OKGREEN}[+]{colors.ENDC} Running module {colors.OKBLUE}({current_module["module_name"]}){colors.ENDC}')
                system(current_module['instruction'])
                print(f'{colors.OKGREEN}[+]{colors.ENDC} Done \n')