import socket, os

shutdown = False
join = False

os.system("clear")
os.system('ifconfig | grep "inet"')

host = "XXX.XXX.XX.X"
port = 0

print("Change IP address?")
userChose = input("Write Y/N: ")

if ((userChose == "Y") or (userChose == "y")):
    host = input("Write IP address: ")

server = ("XXX.XXX.XX.XX", 9999)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

alias = input("NameWord: ")

while shutdown == False:
    if join == False:
        s.sendto(("[" + alias + "] => join chat").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()
            if message != "":
                s.sendto(("[" + alias + "] :: " + message).encode("utf-8"), server)
                data, addr = s.recvfrom(1024)
                print(data.decode("utf-8"))

        except:
            s.sendto(("[" + alias + "] <= left chat").encode("utf-8"), server)
            shutdown = True

s.close()
