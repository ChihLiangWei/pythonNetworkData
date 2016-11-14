import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_42.html'
html = urllib.urlopen(url).read()
#print html
soup = BeautifulSoup(html)
#print soup
#print type(soup)

# Retrieve all of the anchor tags
tags = soup('span')
sum=0
for tag in tags:
    # Sum
    sum=sum+int(tag.contents[0])
print sum
