#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:48:52 2017

@author: kderrick
"""

import socket
import time
import sys
from threading import Thread
from base import commandCentreMonitor
from base import commandCentreOperations

########################################################################

base_control = commandCentreOperations(socket.gethostbyname(''), 9202)
time.sleep(0.5)
base_monitor = commandCentreMonitor(socket.gethostbyname(''), 9203)

thr1 = Thread(target=base_control.command_output_test, args=())
thr2 = Thread(target=base_monitor.test_get_message, args=())


thr1.setDaemon(True)
thr2.setDaemon(True)

thr1.start()
thr2.start()

thr1.join()
thr2.join()

print("Quitting main.")