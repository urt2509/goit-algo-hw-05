 
for activation venv 
PS E:\PyProjects\goit-algo-hw-05> .\venv\Scripts\Activate.ps1 

how to check virtual environment (have to return True)

import sys

def is_virtual_env_active():
    return hasattr(sys, 'real_prefix') or (getattr(sys, 'base_prefix', sys.prefix) != sys.prefix)

print(is_virtual_env_active())
