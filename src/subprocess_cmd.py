import subprocess
from subprocess import call

def execute_cmd(os, cmd):
    if os == "win32":
        comand_prompt = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True, shell=True)
        return comand_prompt
    elif os == "linux64":
        comand_prompt = call(cmd, shell=True)
        return comand_prompt
    else:
        return "OS não listado"
    
    