#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import re

#Found the first download page
url = 'https://www.python.org/downloads/'
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
for releaseChunk in soup.findChildren(class_="release-number"):
    releaseVer = releaseChunk.findChild(text=re.compile('2.7.4'))
    if releaseVer is None:
        continue
    releaseDate = releaseChunk.findNextSibling(class_="release-date", text='April 6, 2013')
    if releaseDate is None:
        continue   
    Dlink = releaseDate.findNextSibling(class_="release-download").find('a').get('href')
    #print(Dlink)

#Now to find download link
url = 'https://www.python.org' + Dlink
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
realLink = soup.find('a', text= re.compile('Windows X86-64 MSI Installer')).get('href')
print(realLink)

#Now to download file
r = requests.get('https://www.python.org' + realLink, allow_redirects=True)
open(realLink.rsplit('/', 1)[1], 'wb').write(r.content)