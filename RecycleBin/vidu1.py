from bs4 import BeautifulSoup
import requests
url = "https://www.google.com/"
respone = requests.get(url)
soup= BeautifulSoup(respone.text, "html5lib")

print( soup.find_all('a'))
