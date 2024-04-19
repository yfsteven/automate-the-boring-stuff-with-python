#! python3
# linkVerification.py - A program to verify every single links of a website

import requests, os, bs4

url = input('Enter a website\n')

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.find_all('a')

for link in links:
    if link.get('href') is not None:
        if 'https:' not in link.get('href') and link.get('href'):
            link_href = url + link.get('href')
            res = requests.get(link_href)
        else:
            res = requests.get(link.get('href'))
        try:
            res.raise_for_status()
            print('Getting %s' % (link_href))
        except Exception as exc:
            print('There was a problem with %s' % (exc))

