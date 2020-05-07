#!/usr/bin/env python3
import sys
import argparse
import socket
import binascii
import base64

# 'argparse' is a very useful library for building python tools that are easy
# to use from the command line.  It greatly simplifies the input validation
# and "usage" prompts which really help when trying to debug your own code.
def main():
    parser = argparse.ArgumentParser(description="Solver for 'All Your Base' challenge")
    parser.add_argument("ip", help="IP (or hostname) of remote instance")
    parser.add_argument("port", type=int, help="port for remote instance")
    args = parser.parse_args()

    # This tells the computer that we want a new TCP "socket"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # This says we want to connect to the given IP and port
    sock.connect((args.ip, args.port))

    # This gives us a file-like view for receiving data from the connection which
    # makes handling messages from the server easier since it handles the
    # buffering of lines for you.  Note that this only helps us on receiving data
    # from the server and we still need to send data over the underlying socket
    # (i.e. `sock.send(...)` at the end of the loop below).
    f = sock.makefile()
    do_stuff(f, sock)

def do_stuff(f, sock):
    while True:
        data = ''
        conversion = ''
        almostanswer = ''
        while '-'*78 not in data:    
            data = f.readline().strip('\n')
            print(data)
        if '-'*78 in data:
            print(data)
        conversion = f.readline().strip().split(' -> ')
        print(conversion)
        almostanswer = f.readline().strip()
        print(almostanswer)
        count = 0
        tmpconversion = conversion[0]
        while count < 7:
            if tmpconversion == 'dec':
                almostanswer = dec2oct(almostanswer)
                tmpconversion = 'oct'
                if conversion[1] == tmpconversion:
                    sendanswer(almostanswer, f, sock)
                count = count + 1
            if tmpconversion == 'oct':
                almostanswer = oct2bin(almostanswer)
                tmpconversion = 'bin'
                if conversion[1] == tmpconversion:
                    sendanswer(almostanswer, f, sock)
                count = count + 1
            if tmpconversion == 'bin':
                almostanswer = bin2hex(almostanswer)
                tmpconversion = 'hex'
                if conversion[1] == tmpconversion:
                    sendanswer(almostanswer, f, sock)
                count = count + 1
            if tmpconversion == 'hex':
                almostanswer = hex2b64(almostanswer)
                tmpconversion = 'b64'
                if conversion[1] == tmpconversion:
                    sendanswer(almostanswer, f, sock)
                count = count + 1
            if tmpconversion == 'b64':
                almostanswer = b642raw(almostanswer)
                tmpconversion = 'raw'
                if conversion[1] == tmpconversion:
                    sendanswer(almostanswer, f, sock)
                count = count + 1
            if tmpconversion == 'raw':
                almostanswer = raw2dec(almostanswer)
                tmpconversion = 'dec'
                if conversion[1] == tmpconversion:
                    sendanswer(almostanswer, f, sock)
                count = count + 1

def dec2oct(almostanswer):
    answer = oct(int(almostanswer)).replace('0o', '')
    print(answer)
    return answer

def oct2bin(almostanswer):
    answer = bin(int(almostanswer, 8)).replace('0b', '')
    print(answer)
    return answer

def bin2hex(almostanswer):
    answer = hex(int(almostanswer, 2)).replace('0x','')
    print(answer)
    return answer

def hex2b64(almostanswer):
    answer = base64.b64encode(binascii.unhexlify(bytes(almostanswer, encoding='ascii'))).decode()
    print(answer)
    return answer

def b642raw(almostanswer):
    answer = base64.b64decode(almostanswer).decode()
    print(answer)
    return answer

def raw2dec(almostanswer):
    answer = str(int(binascii.hexlify(bytes(almostanswer, encoding='ascii')).decode('ascii'), 16))
    print(answer)
    return answer

    #  raw = the unencoded ASCII string (contains only printable characters
     #               that are not whitespace)
      #    b64 = standard base64 encoding (see 'base64' unix command)
       #   hex = hex (base 16) encoding (case insensitive)
        #  dec = decimal (base 10) encoding
         # oct = octal (base 8) encoding
          #bin = binary (base 2) encoding (should consist of ASCII '0' and '1')

def sendanswer(answer, f, sock):
    f.readline().strip('\n')
    print(answer)
    sock.send((answer + "\n").encode()) # The "\n" is important for the server's
    do_stuff(f, sock)
                                            # interpretation of your answer, so make
                                        # sure there is only one sent for each
                                            # answer.
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()