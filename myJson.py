import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_324258.json'
uh = urllib.urlopen(url)
data = uh.read()
print data
info = json.loads(data)
print 'User count:', len(info["comments"])
total=0
for item in info["comments"]:
    print 'Name:', item["name"]
    print 'Count:', item["count"]
    total=total+item["count"]
print 'Total:', total

