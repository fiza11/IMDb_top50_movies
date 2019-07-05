import requests
from bs4 import BeautifulSoup
year1 = input("Enter 1st year")
year2 = input("Enter 2nd year")
if (year2 < year1):
	a = year1
	year1 = year2
	year2 = a
url = "https://www.imdb.com/search/title/?release_date=" + year1 + "," + year2 + "&title_type=feature"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
list = soup.findAll('h3', attrs={'class':'lister-item-header'})
f = 1
for i in list:
	a_tag = i.find('a')
	movie = a_tag.text
	print(f, end = ". ")
	print(movie)
	f += 1

