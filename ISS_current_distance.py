#!/usr/bin/env python

import urllib, json, threading, math
# open source API for tracking the ISS
url= 'https://api.wheretheiss.at/v1/satellites/25544'
#Input your local GPS coordinates here in order to get an accurate distance
home_lat = 40.7295733
home_long = -74.00466599
def work(home_lat, home_long):
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        iss_lat = data['latitude']
        iss_long = data['longitude']
        distance = sph_dist(home_lat, home_long, iss_lat, iss_long)
        printCoordinates(distance, home_lat, home_long, iss_lat, iss_long)
        # threading.Timer(30, work(home_lat, home_long)).start()
def printCoordinates(distance, home_lat, home_long, iss_lat, iss_long):
        # print "The International Space Station current coordinates are "
        # print "Latitude =",iss_lat," ","Longitude =",iss_long
        # print "Current distance to the ISS: ",distance
        print distance
        # print ""
        # print "=================================="
# Compute spherical distance from spherical coordinates. Based on the work of mathematician John D. Cook at http://www.johndcook.com/blog/python_longitude_latitude/ 
def sph_dist(lat1, long1, lat2, long2):
        degrees_to_radians = math.pi/180.0
        phi1 = (90.0 - lat1)*degrees_to_radians
        phi2 = (90.0 - lat2)*degrees_to_radians
        theta1 = long1*degrees_to_radians
        theta2 = long2*degrees_to_radians
        cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + math.cos(phi1)*math.cos(phi2))
        arc = math.acos( cos )
        return arc * 3960
work (home_lat, home_long)

