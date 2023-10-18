import paramiko
import logging
# Set Paramiko logging level to DEBUG
paramiko.util.log_to_file("paramiko.log")
logging.getLogger("paramiko").setLevel(logging.DEBUG)

server = ''

user = ''
password = ''

i = '/home/teddy/Desktop/website_resume.pdf'

try:
    transport = paramiko.Transport((server, 22))
    transport.connect(username=user, password=password)
    sftp = transport.open_sftp_client()

    sftp.put(i, 'website_resume.pdf')
    # files = sftp.listdir('/')
    # print(files)
    # for i in file:
    #     sftp.putfo(i, f'/{container}/{i.name}')

    sftp.close()
    transport.close()
except Exception as e:
    print(e)
    



