import requests
from bs4 import BeautifulSoup as bs
import urllib.request, urllib.error, urllib.parse

URL = 'https://www.google.com/covid19/mobility/' 

# functional
r = requests.get(URL)
soup = bs(r.text, "lxml")
urls = []
names = []
for i, link in enumerate(soup.findAll('a')):
    FULLURL = link.get('href')

    if FULLURL.endswith('.pdf'):
        print(FULLURL)
        soupPDFLink = soup.select('a')[i].attrs['href']

        urls.append(FULLURL)
        names.append(soupPDFLink.rsplit("/", 1)[-1])
print(len(urls))

names_urls = list(zip(names, urls))

for name, url in names_urls:
    rq = urllib.request.Request(url)
    res = urllib.request.urlopen(rq)
    pdf = open("pdfs/" + name, 'wb')
    pdf.write(res.read())
    pdf.close()


