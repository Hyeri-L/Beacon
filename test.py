# -*- coding: utf-8 -*-
# test BLE Scanning software
# jcs 6/8/2014


import blescan
import sys

import bluetooth._bluetooth as bluez

dev_id = 0
try:
        sock = bluez.hci_open_dev(dev_id)
        print "ble thread started"

except:
        print "error accessing bluetooth device..."
        sys.exit(1)

blescan2.hci_le_set_scan_parameters(sock)
blescan2.hci_enable_le_scan(sock)

while True:
        returnedList = blescan2.parse_events(sock, 10)
        print "----------"
        for beacon in returnedList:
                if beacon[:17] == '00:19:01:70:81:': #특정 비콘을 선택해서 출력
                        print beacon

