import urllib
import xml.etree.ElementTree as ET

address = 'http://python-data.dr-chuck.net/comments_324254.xml'
print 'Retrieving', address
uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
commentinfo = ET.fromstring(data)

counts = commentinfo.findall('comments/comment')
#print type(counts)
total=0
for item in counts:
    total=total+int(item.find('count').text)
print total
