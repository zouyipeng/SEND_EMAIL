#!/usr/bin/python
import time
import requests
a=10
for num in range(0,100):
    a+=num
    print(a,num,time.time())
print(a)