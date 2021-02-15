######## Copy files to remote server using SFTP ######## 

# assuming rsa key is added key is added
with pysftp.Connection('127.0.0.1', username='sftp.user') as sftp:
            with sftp.cd('/SAMPLE/OUTPUT'):
                # upload files to sftp dir
                sftp.put(samplefile)
                
######## Copy files to remote server using FTP ######## 
import ftplib
 
ftp = ftplib.FTP("ftp.nluug.nl")
ftp.login("anonymous", "ftplib-example-1")
 
data = []
 
ftp.dir(data.append)
 
ftp.quit()


######## Copy files to remote server using SCP ######## 
from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('example.com')

# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())

scp.put('test.txt', 'test2.txt')
scp.get('test2.txt')

# Uploading the 'test' directory with its content in the
# '/home/user/dump' remote directory
scp.put('test', recursive=True, remote_path='/home/user/dump')

scp.close()
