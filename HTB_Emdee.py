import requests
import hashlib
import re
from bs4 import BeautifulSoup

url = "http://docker.hackthebox.eu:30391/"
req = requests.session()

r = req.get(url)
soup = BeautifulSoup(r.text,"html.parser")
sel = soup.find("h3")
hash = sel.text
de = hashlib.md5(hash.encode('utf-8')).hexdigest()

data = dict(hash=de)
rp = req.post(url=url, data=data)
print(rp.text)
