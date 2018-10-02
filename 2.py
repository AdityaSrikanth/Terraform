import os

from pexpect import popen_spawn

user = 'AdityaSrikanth'
password = 'Loginadi@7a'

os.system('git add .' )
os.system('git commit -m "Added 2file"')
# os.system('$Username = "AdityaSrikanth"')
os.system('git config credential.helper store')
cmd = os.system('git push https://github.com/AdityaSrikanth/Terraform.git')
child_process = popen_spawn.PopenSpawn(cmd)
child_process.expect('User')
child_process.sendline(user)
child_process.expect('Password')
child_process.sendline(password)


