from encodings import utf_8
import subprocess
import re
command1 = "netsh wlan show profiles"
profiles = subprocess.check_output(command1,shell=True)

names = re.findall("(?:Profile\s*\:\s)(.*)",profiles.decode('utf-8'))

result = ""
for name in names : 
    nx = '"' + name + '"'
    command2 = "netsh wlan show profile name = " + nx + " key=clear"
    result2 = subprocess.check_output(command2,shell=True)
    result = result + result2.decode('utf-8')

print(result)