import re
from bs4 import BeautifulSoup
import requests

r = requests.get("https://google.com/search?q=python-beautiful-soup")
html = re.sub("[^a-zA-Z0-9\.\,\:\;\<\>\-\+\=\*\"\' \n\{\}]", "", r.text)
#with open("test2.html", "w", encoding="utf-8") as f:
	#f.write(html)

soup = BeautifulSoup(html, "lxml")
print(soup.find_all("cite"))

def fetch_results(query):
	search = "https://google.com/search?q=" + query
	resp = requests.get(search).text
	print(resp)
	soup = BeautifulSoup(resp, "lxml")
	links = soup.findAll(class_="iUh30 Zu0yb qLRx3b tjvcx")
	print(links)

#fetch_results("python convert mp3 to wav")