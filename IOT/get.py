import urllib2
import re

req1 = urllib2.Request('http://api.mediatek.com/mcs/v2/devices/DZ1hv7XW/datachannels/latitude/datapoints.csv?limit=1000')
req1.add_header('DeviceId', 'DZ1hv7XW')
req1.add_header('DeviceKey', 'Zi6PgULxLcJCSoGv')
resp1 = urllib2.urlopen(req1)
content1 = resp1.read()

req2 = urllib2.Request('http://api.mediatek.com/mcs/v2/devices/DZ1hv7XW/datachannels/longitude/datapoints.csv?limit=1000')
req2.add_header('DeviceId', 'DZ1hv7XW')
req2.add_header('DeviceKey', 'Zi6PgULxLcJCSoGv')
resp2 = urllib2.urlopen(req2)
content2 = resp2.read()

list1 = re.split(',|\r\n', content1)
list2 = re.split(',|\r\n', content2)
f = open('GPSdata', 'w')

j = 1
for i in range(min(len(list1), len(list2)) - 1, 2, -3):
    if i == min(len(list1), len(list2)) - 1:
        f.write("['bump'," + str(float(list1[i]) / 10000) + ',' + str(float(list2[i]) / 10000) + ',' + str(j) + ']\n')
    else:
        f.write(",['bump'," + str(float(list1[i]) / 10000) + ',' + str(float(list2[i]) / 10000) + ',' + str(j) + ']\n')
    j += 1



# print list
