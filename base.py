#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:48:23 2017

@author: kderrick
"""

"""
Created on Fri May 26 17:59:32 2017

@author: kderrick
"""

import socket
import time
import sys

class commandCentreMonitor:
    #Need to create two instances. Create CommandCentreOperations and CommandCentreSensors
    
    def __init__(self, host_receive, port_receive):
        global client

        #Create client for receiving
        print("Initializing Ciommand Center Monitor...")
    
        # create a socket object
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Created")
        
        # connection to hostname on the port.
        try:
            print ("Trying...")
            client.connect((host_receive, port_receive))
            print("connected..")
        except socket.error as msg:
            print("FAILED to connect")
    
    def test_get_message(self):
         while True:
         # Receive no more than 1024 bytes
             message = client.recv(4096)
             if ( ":Q" in message.decode('ASCII')):
                 sys.stdout.flush()
                 time.sleep(2) 
                 print("closing.." + message.decode('ASCII'))
                 print("Ending threrad...")
                 client.close()
                 break
             #Next message to print
             else:
                 print(message.decode('ascii'))
                 sys.stdout.flush()
    
class commandCentreOperations:  
    def __init__(self, host_send, port_send):
        global server
    

        #Create server for sending
        print("Initializing CommandCenter Operations ...")
        
        # create a socket object
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind to the port
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind((host_send, port_send))
        
        print("Bound..")
    
        serversocket.listen(5)
        
        # establish a connection
        server,addr = serversocket.accept()
        
        print("Got a connection from %s" % str(addr))
        
        print("Got connect")
        
    def send(self, message):
        server.send(message.encode('ascii'))
        
    def command_output_test(self):
        i = 0
        while True:
            message = "This is message #" + str(i) + " a different test \n\r"
            if i  == 300:
                message = ":Q"
                server.send(message.encode('ASCII'))
                break
            else:
                server.send(message.encode('ASCII'))
            i +=1
        
    def disconnect(self):
        server.close()
            