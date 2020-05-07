#/usr/bin/env python3

from pathlib import Path
import collections

def iptodecimal(data):
    with open('/root/Downloads/ips.txt', 'r') as ipsfile:
        iplist = ipsfile.readlines()
        for ip in iplist:
            octets = ip.split('.')
            hexjoin = ''
            for i in octets:
                hexjoin = hexjoin + hex(int(i.replace('\n', ''))).replace('0x', '')
            compare(hexjoin, data)

def compare(hexjoin, data):
    ipdecimal = int(hexjoin, 16)
    max = len(data) - 1
    min = 0
    while True:
        print(binsearch)
        line = data[max]
        lineitems = line.split(',')
        lower = lineitems[0].replace("\"", "")
        higher = lineitems[1].replace("\"", "")
        if lower == '0':
            lower = '1'
        if ipdecimal >= int(lower) and ipdecimal <= int(higher):
            appendresults(lineitems[3].replace("\"", "").strip())
            return
        if ipdecimal > int(higher) and ipdecimal :
            max = 
            binsearch += binsearch / 2
            int(binsearch)
        if ipdecimal < int(lower) :
            binsearch = binsearch / 2
            int(binsearch)



def appendresults(country):
    with open('/root/Downloads/results', 'a+') as resultfile:
        resultlines = resultfile.readlines()
        resultlines.append(country + '\n')
        resultfile.writelines(resultlines)
        return
        

def main():
    path2results = Path('/root/Downloads')
    path2results.touch('results.txt')
    with open('/root/Downloads/IP2LOCATION-LITE-DB1.CSV', 'r') as f:
        data = f.readlines()
        iptodecimal(data)
    with open('results', 'r') as printresults:
        counts = collections.Counter(l.strip() for l in printresults)
    for line, count in counts.most_common():
        print(line + ': ' + count)    

if __name__ == "__main__":
    main()


