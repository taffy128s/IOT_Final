import os

text1 = open('test1', 'r')
text2 = open('test2', 'r')
data = open('GPSdata', 'r')
final = open('final.html', 'w')



final.write(text1.read() + data.read() + text2.read())
