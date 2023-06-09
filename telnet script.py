
# the below two libraries are imported into pyth
import getpass
import telnetlib
# the below is the  ip address of  R1
HOST = "192.168.122.71"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
# the below commands are to carry out CLI commands
tn.write(b"enable\n")
tn.write(b"devnet\n")
tn.write(b"conf t\n")
tn.write(b"interface loopback 1\n")
tn.write(b"ip address 7.7.7.7 255.255.255.255 \n")
tn.write(b"interface loopback 2\n")
tn.write(b"ip address 6.6.6.6 255.255.255.255 \n")
tn.write(b" end \n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))