

import bs4
from bs4 import BeautifulSoup
import requests 
import numpy as np 
import pandas as pd
import re
import geopy
import time
from geopy.geocoders import Nominatim





def getCoordinates(address):
    counter= 0
    geolocator =Nominatim(user_agent="my_request")
    time.sleep(0.0010)
    location = geolocator.geocode(address)

    if location:
        latit=location.latitude
        longit =location.longitude
    else:
        list = address.split(",")
        length =len(list)
        addressArea=list[length-2]
        
        print("second last array element ",list[length-2])
        location=geolocator.geocode(addressArea)
        if location:
            latit=location.latitude
            longit =location.longitude
        else:
            print("--ADDRESS LOCATION NOT FOUND",address)
            latit=0
            longit =0
    return(latit,longit)



def main():
   
   address=("5 Beresford House, Custom House Square, IFSC, Dublin 1")
   (latit,longit)=getCoordinates(address)
   print("Testing to see if its address or sys over load , coords are",latit,longit)
   return 0;

if __name__ == '__main__':
    main()