import urllib2

response = urllib2.urlopen('http://www.gutenberg.org/files/135/135-h/135-h.htm')
html = response.read()


print html