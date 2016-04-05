import netifaces
import socket
import getpass

def identity():
    user = getpass.getuser()
    hostname = socket.gethostname()
    ipaddrs = []
    for interface in netifaces.interfaces():
        try:
            for addr in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                ipaddrs.append(addr['addr'])
        except KeyError:
            pass
        try:
            for addr in netifaces.ifaddresses(interface)[netifaces.AF_INET6]:
                ipaddrs.append(addr['addr'])
        except KeyError:
            pass
    ip = ','.join(ipaddrs)
    return (user, hostname,ip)

def retrieve_user():
    user = input("Username: ")
    password = getpass.getpass()
    return (user, password)
