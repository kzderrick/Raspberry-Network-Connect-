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
from rov import RovControlHub
from rov import RovSensorRelay

########################################################################

rov_control = RovControlHub(socket.gethostbyname(''), 9202)
rov_sensors = RovSensorRelay(socket.gethostbyname(''), 9203)

thr1 = Thread(target=rov_control.test_get_message, args=())
thr2 = Thread(target=rov_sensors.relay_sensor_output_test, args=())


thr1.setDaemon(True)
thr2.setDaemon(True)

thr1.start()
thr2.start()

thr1.join()
thr2.join()