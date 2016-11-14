import urllib
import re

# 1. print Version 1
#fhand = urllib.urlopen('http://python-data.dr-chuck.net/regex_sum_324252.txt')
#for line in fhand:
#    print line.strip()
    
# 2. print Version 2
#fhand = urllib.urlopen('http://python-data.dr-chuck.net/regex_sum_324252.txt')
#print fhand.read()

# 3. Print sum of all the number in the file
fhand = urllib.urlopen('http://python-data.dr-chuck.net/regex_sum_324252.txt')
print(sum([int(x) for x in re.findall('[0-9]+',fhand.read())]))
