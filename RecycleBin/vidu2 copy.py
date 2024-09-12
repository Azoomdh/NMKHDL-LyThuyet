# lam dep html
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story" id="linkP" id2="AAA">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="story" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story" id="linkP" id2="AAA">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html5lib')

"""
a= soup('p', {'class':'story'}, id='linkP', id2="AAA" )
print(a[1].id)
"""

a= soup('a')
print(a[1]])