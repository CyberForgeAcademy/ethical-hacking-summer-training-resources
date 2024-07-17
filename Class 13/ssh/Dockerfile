# Use the official Ubuntu base image
FROM ubuntu:latest

# Install OpenSSH server and sudo
RUN apt-get update && apt-get install -y openssh-server sudo

# Create the necessary directories for SSH
RUN mkdir /var/run/sshd

# Add users 'alice' and 'jack' with their respective passwords
RUN useradd -m -s /bin/bash alice && echo "alice:zaq12wsx" | chpasswd
RUN useradd -m -s /bin/bash jack && echo "jack:1q2w3e" | chpasswd

# Allow password authentication and root login
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Copy the secret.txt file to jack's home directory and set the correct permissions
COPY secret.txt /home/jack/secret.txt
RUN chown jack:jack /home/jack/secret.txt && \
    chmod 600 /home/jack/secret.txt

# Expose the SSH port
EXPOSE 22

# Start the SSH service
CMD ["/usr/sbin/sshd", "-D"]
