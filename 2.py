import os

from pexpect import popen_spawn

user = 'AdityaSrikanth'
password = 'Loginadi@7a'

os.system('git add .' )
os.system('git commit -m "Added 2file"')
# os.system('$Username = "AdityaSrikanth"')
os.system('git config credential.helper store')
os.system('git push https://github.com/AdityaSrikanth/Terraform.git')
os.system("echo AdityaSrikanth")

