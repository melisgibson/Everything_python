from urllib.request import ssl, socket
import datetime, smtplib

print(f"Program to check SSL certificate validity and expiration date\n")

##opening file
ipfile = open("server_ip.txt")

##check  certificate expiration
for ip in ipfile:
    try:
        host = ip.strip().split(":")[0]
        port = ip.strip().split(":")[1]
        print(f"\nChecking certifcate for server {host}")
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                certificate = ssock.getpeercert()
                print(f"Version: {ssock.version()}")
            certExpires = datetime.datetime.strptime(
                certificate["notAfter"], "%b %d %H:%M:%S %Y %Z"
            )
            daysToExpiration = (certExpires - datetime.datetime.now()).days
            print(f"Expires on: {certExpires}")
            print(f"In {daysToExpiration} days")

    except:
        print(f"error on connection to Server, {host}")


print(f"\nCert check complete!")