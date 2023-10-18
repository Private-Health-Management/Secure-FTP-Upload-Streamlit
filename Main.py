import streamlit as st
import paramiko

st.title('Secure FTP Upload Form')

server = st.text_input('Please enter the server name')
user = st.text_input('Please Enter your username')
password = st.text_input('Please enter your password')

file = st.file_uploader('Please Upload your Files here', accept_multiple_files=True)

if st.button('Upload Files'):
    if len(server) > 0 and len(user) > 0 and len(password) > 0 and len(file) > 0:
        try:
            transport = paramiko.Transport((server, 22))
            transport.connect(username=user, password=password)
            sftp = transport.open_sftp_client()

            for i in file:
                sftp.putfo(i, str(i.name))

            # if we want to assume that the directory starts empty and cannot be appended, use this code
            # if len(sftp.listdir('/')) > 0:
            #     st.text('Upload Successful, Thank You!')
            #     sftp.close()
            #     transport.close()

            # otherwise, use this
            st.text('Upload Successful, Thank You!')
            sftp.close()
            transport.close()
            
        except Exception as e:
            st.error(f'Error: {e}.  If this error persists and the correct field has been inputted, please contact PHM.')
            print(e)
    else:
        st.error('Please Fill out all Forms and Upload at least one File')
    




