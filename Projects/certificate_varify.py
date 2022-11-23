import ssl
import socket
import datetime

print(f"Program to check SSL certificate validity and expiration date\n")

##opening file
with open("server_ip.txt") as ip_file:

    ##check  certificate expiration
    for ip in ip_file:
        try:
            host, port = ip.strip().split(":")
            print(f"\nChecking certifcate for server {host}")
            context = ssl.create_default_context()
            with socket.create_connection((host, port)) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    certificate = ssock.getpeercert()
                certExpires = datetime.datetime.strptime(
                    certificate["notAfter"], "%b %d %H:%M:%S %Y %Z"
                )
                daysToExpiration = (certExpires - datetime.datetime.now()).days
                print(f"Expires on: {certExpires} in {daysToExpiration} days")

        except:
            print(f"error on connection to Server, {host}")


print(f"\nCert check complete!")
