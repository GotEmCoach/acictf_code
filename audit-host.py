#!/usr/bin/env python3

import re
import binascii

def main():
    with open('/root/Downloads/audit.log', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'proctitle' in line:
                items = line.split(' ')
                for item in items:
                    if 'proctitle' in item and 'proctitle=\"load_policy\"' not in item:
                        if len(item.replace('proctitle=', '')) % 2 != 0:
                            item = item[:-1]
                        converted = 'proctitle=' + str(binascii.a2b_hex(item.replace('proctitle=', '')))
                        print(line.replace(item, converted))
            if 'saddr' in line:
                    items = line.split(' ')
                    for item in items:
                        if 'saddr' in item:
                            if len(item.replace('saddr=', '')) % 2 != 0:
                                item = item[:-1]
                            converted = 'saddr=' + str(binascii.a2b_hex(item.replace('saddr=', '')))
                            print(line.replace(item, converted))
            
        #ip_candidates = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", data)
        #other_ips = re.findall(r"\d{1,3}\-\d{1,3}\-\d{1,3}\-\d{1,3}\b", data)
        #for i in ip_candidates:
        #    if i != '10.0.2.2' and i != '10.0.2.15':
        #        print(i)
        #for i in other_ips:
        #    print(i)
if __name__ == "__main__":
    main()