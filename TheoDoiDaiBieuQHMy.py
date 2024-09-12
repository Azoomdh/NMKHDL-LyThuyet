print("Vi du: theo doi dai bieu quoc hoi My")
print("thu thap va chuyen doi text thanh doi tuong BeautifulSoup")

print("#---------------------------------------")
from bs4 import BeautifulSoup
import requests
import re

url = "https://www.house.gov/representatives" 
respone= requests.get(url) 
soup = BeautifulSoup(respone.text, 'html5lib')
print("#---------------------------------------")
print("thu thap moi the a ma co chua link href")
listUrl= []
for a in soup('a') :
	if (a.has_attr('href') ):
		listUrl.append(a['href'] ) 
	#
#
print(len(listUrl) )

print("#---------------------------------------")

print("URL phai bat dau boi: http:// hoac https:// ")
print("URL phai ket thuc boi: .house.gov	hoac .house.gov/.")

regex = r"^https?://.*\.house\.gov/?$"
selectedUrl= []
for u in listUrl :
	if (re.match(regex, u)== True ):
		selectedUrl.append(u )
	#
#
print("#---------------------------------------")
print("Loai bo url trung lap")
from typing import Dict, Set

selectedUrl= list(set(selectedUrl) )
print("#---------------------------------------")
print("Thu thap url gan voi link cua trang web goc")
press_releases: Dict[str, Set[str] ]= { }
for house_url in selectedUrl:
	html = requests.get(house_url ).text
	soup= BeautifulSoup(html, 'html5lib')
	pr_links= { }
	for a in soup('a') :
		if 'press release' in a.text.lower() :
			pr_links.append(a )
		#
	#
	press_releases[house_url ]= pr_links
#
print("#---------------------------------------")
print("Trang web co tan suat thu thap duoc phep")
print("Trang web co cac url khong duoc phep thu thap")
print("#---------------------------------------")
print("Tra ve True neu van ban text (text la dang html) co chua tu khoa str")
def paragraph_mentions(text: str, keyword: str )->bool :
	soup= BeautifulSoup(text, 'html5lib' )
	paragraphs= []
	for p in soup('p') :
		paragraphs.append(p.get_text() )
	#
	for pa in paragraphs :
		if keyword.lower() in pa :
			return True
		#
	#
	return False
#
print("#---------------------------------------")
print("Thu nghiem: tim nhung dai bieu da de cap ve keyword= 'data'")
for house_url, pr_links in press_releases.items( ) :
	for pr_link in pr_links :
		url= f"{house_url}/{pr_link}"
		text= requests.get(url).text
		keyword= 'data'
		if ( paragraph_mentions(text, keyword )== True ) :
			print(f"{house_url}")
			break #thoat for cua pr_link
		#
	#
#
