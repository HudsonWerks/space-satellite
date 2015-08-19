##plot the location of the ISS with updates every 60 seconds. Based on Damian Mooney's script at https://damianmooney.wordpress.com/2014/05/11/python-and-the-iss-part-2/ and API from Open Notify at http://open-notify.org/Open-Notify-API/ISS-Location-Now/

import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime
import time
import urllib2
import json

def getiss():
    #call opennotify api
    response = urllib2.urlopen('http://api.open-notify.org/iss-now.json')
    mydata = response.read()
    return(mydata)

while True:
    iss = getiss()
    pos = json.loads(iss)
    lat = pos['iss_position']['latitude']
    lon = pos['iss_position']['longitude']

    # miller projection
    map = Basemap(projection='mill',lon_0=0)
    # plot coastlines, draw label meridians and parallels.
    map.drawcoastlines()
    map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])
    # fill continents 'coral' (with zorder=0), color wet areas 'aqua'
    map.drawmapboundary(fill_color='aqua')
    map.fillcontinents(color='coral',lake_color='aqua')
    # shade the night areas, with alpha transparency so the
    # map shows through. Use current time in UTC.
    date = datetime.now()
    CS=map.nightshade(date)
    plt.title('ISS Location for %s Lat: %.2f Long: %.2f' % (date.strftime("%d %b %Y %H:%M:%S"),lat,lon))

#   Add prediction location string here

#Sets the coordinates for the point we want to plot and then plots it on a map as a blue circle sized 12.
    x,y = map(lon, lat)
    map.plot(x, y, 'bo', markersize=12)
    plt.ion()
    plt.draw()
    plt.show(block=False)
    time.sleep(60) #limit updates to once per minute
    plt.clf()
