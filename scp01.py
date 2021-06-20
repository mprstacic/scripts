import paramiko; from paramiko import SSHClient
from scp import SCPClient
import getpass

ssh = SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #optional once ssh key added to known_hosts
ssh.load_system_host_keys()

filename = input("Enter source file name: ")
ip = input("Enter destination IP: ")
user = input("Username: ")
pswd = getpass.getpass("Password: ")
ssh.connect(ip, username=user, password=pswd)

scp = SCPClient(ssh.get_transport())
print("Copying files to %s: ..." % (ip))
scp.put(filename ,recursive=False, remote_path='/home/mprstacic/')
#scp.put('./folder_name',recursive=True,  remote_path='/var/www/html/folder_name')
scp.close()
print("Done.")
