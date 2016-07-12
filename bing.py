from bs4 import BeautifulSoup
import requests
r = requests.get("http://www.bing.com")
soup = BeautifulSoup(r.text, "html.parser")
text= (soup.prettify()).encode('utf-8')
instance = soup.find_all("script", {"type": "text/javascript"})
for i in instance:
	if "g_img" in i:
		print i
