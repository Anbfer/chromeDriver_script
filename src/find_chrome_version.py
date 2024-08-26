import subprocess_cmd
import re

def define_chrome_version(system_os):
    
    version_pattern = re.compile(r'[0-9]+\.[0-9]+\.[0-9]+(?:\.[0-9]+)?')
    not_found = "versão do Chrome não identificada"
    
    if system_os != "linux64":
        command = 'reg query "HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon" /v version'
        output = subprocess_cmd.execute_cmd(system_os, command).stdout
        match = version_pattern.search(output)
        if match:
            return match.group(0)
        else:
            return not_found
    else:
        command = 'google-chrome --version'
        output = subprocess_cmd.execute_cmd(system_os, command).stdout
        match = version_pattern.search(output)
        if match:
            return match.group(0)
        else:
            return not_found