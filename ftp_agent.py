import ftplib

# FTP server details
ftp_host = "0.0.0.0"
ftp_user = "<username>"
ftp_pass = "<password>"

# Connect to the FTP server
ftp = ftplib.FTP(ftp_host)

# Login to the FTP server
ftp.login(user=ftp_user, passwd=ftp_pass)

# Print the welcome message
# print(ftp.getwelcome())

# List the files and directories in the current directory
ftp.retrlines('LIST')

# Change to a different directory (optional)
# ftp.cwd('/path/to/directory')

# # Download a file from the FTP server
# filename = "example.txt"
# with open(filename, "wb") as file:
#     ftp.retrbinary(f"RETR {filename}", file.write)

# # Upload a file to the FTP server
# upload_filename = "upload_example.txt"
# with open(upload_filename, "rb") as file:
#     ftp.storbinary(f"STOR {upload_filename}", file)

# Close the connection
ftp
