# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:06:53 2022

@author: aerom
"""


import random
#temperature generation
t=random.randint(1,200)
#humidity generation
h=random.randint(1,100)
if(t>100):
    print("ALERT!ALARM ON, temperature is high")
else:
    print("NORMAL ,ALARM OFF ,fine temperature")