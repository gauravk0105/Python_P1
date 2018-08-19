#!usr/bin/python

import requests
from bs4 import BeautifulSoup
url = raw_input("Your Query : ")
page = requests.get("https://www.google.dz/search?q="+url)
soup = BeautifulSoup(page.content,"html.parser")
links = soup.findAll("a")
print "Fetching Top 5 URL......"
for index in range(0,5):
    print index+1,links[index]['href'].encode("utf-8")

execfile ('menu.py')
    
