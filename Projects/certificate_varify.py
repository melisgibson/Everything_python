import ssl
import socket
import datetime

print("Program to check SSL certificate validity and expiration date \n")

# opening file
with open('server_ip.txt') as ip_file:

    # check  certificate expiration
    for ip in ip_file:
        try:
            host = ip.strip().split(":")[0]
            port = int(ip.strip().split(":")[1])
            print("\nChecking certificate for {}".format(host))
            context = ssl.create_default_context()
            with socket.create_connection((host, port)) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    certificate = ssock.getpeercert()
                    print("Version: {}".format(ssock.version()))
                certExpires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
                daysToExpiration = (certExpires - datetime.datetime.now()).days
                print("Expires on: {}".format(certExpires))
                print("In {} days".format(daysToExpiration))

        except Exception as e:
            print("Unknown error occurred {}.".format(e))

print("\nCert check complete!")