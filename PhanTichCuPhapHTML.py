from bs4 import BeautifulSoup
import requests

url = ("https://raw.githubusercontent.com/"
 "joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

print("#-------------------------------------------")

def timTheDauTienTrongSoup(soup, s):
    a= soup.find(s)
    print(a)
#
timTheDauTienTrongSoup(soup, 'p')

print("#-------------------------------------------")
print("hien thi text")
a= soup.find('p')
str= a.text
print(str)
print(str.split())

print("#-------------------------------------------")

print("lay toan bo the thoa man: la p, class=story, id='linkP', id2='AAA'")
a= soup('p', {'class':'story'}, id='linkP', id2= 'AAA')
print(a)

print("#-------------------------------------------")

print("Lay thuoc tinh id cua 1 the p")
listA= soup('p' )
x= listA[0]
idCuaX= x['id']
print(idCuaX)

print("#-------------------------------------------")

print("lay moi the span o trong div")
listSpan= []
for d in soup('div') :
    for s in d('span') :
        listSpan.append(s)
    #
#
print(listSpan)

print("#-------------------------------------------")


