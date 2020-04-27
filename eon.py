import os
import time
import sys
from pubnub import Pubnub
import Adafruit_DHT as dht

pubnub = Pubnub(publish_key='#####', subscribe_key='sub-c-02190da8-ebc6-11e9-bdee-36080f78eb20')

#published in this fashion to comply with Eon
while True:

    h,c = dht.read_retry(dht.DHT11, 4)
    h   = float(h)
    c   = float(c)
    f   = (c*1.8)+32

    pubnub.publish('thompson-hydroponics-temp', {'eon':{
        'celcius':      c,
        'farenheight':  f,
        'humidity':     h
    }})

    time.sleep(900) # 15 minutes
