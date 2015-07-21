import sys
import urllib

name = raw_input("""
Enter search terms ->
""")

url = "https://duckduckgo.com/html/?q="
search = url + name
sock = urllib.urlopen(search)

raw_html = sock.readlines()


try:
    f = open('results.txt', 'a')
    for line in raw_html:
	if 'href="https' in line:
            f.write(line)
except:
    print"nope"

print "done"
