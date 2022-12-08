
from urllib import request, error
from bs4 import BeautifulSoup

with request.urlopen('https://akipress.org') as resp:
    data = resp.read()
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('a', attrs={'class': 'newslink'})
    for item in items:
        print(item.get('htef'))
