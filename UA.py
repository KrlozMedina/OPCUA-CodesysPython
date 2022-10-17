# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:56:00 2020

@author: 
"""
from opcua import Server
from random import randint
import datetime
import time

server=Server()
url="opc.tcp://127.0.0.1:4840"
server.set_endpoint(url)

name="urn:DESKTOP-AT13LUC:UnifiedAutomation:UaExpert"
addspace=server.register_namespace(name)

node=server.get_objects_node()

Param=node.add_object(addspace,"Parameters")

Temp=Param.add_variable(addspace,"Temperature",0)
Press=Param.add_variable(addspace,"Pressure",0)
Time=Param.add_variable(addspace,"Time",0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

server.start()
print("server startet at {}".format(url))

while (True):
    Temperature=randint(10,50)
    Pressure=randint(200,999)
    TIME=datetime.datetime.now()
    print(Temperature,Pressure,TIME)
    
    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)
    
    time.sleep(2)
