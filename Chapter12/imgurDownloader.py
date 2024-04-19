#! python3
# imgurDownloader - Downloads all resulting images of your chosen category on Imgur
import requests, os, bs4, urllib.request
url = 'https://imgur.com/search/score?q='
input_text = input('What image you want?\n')
res = requests.get(url + '+'.join(input_text.split(' ')))
res.raise_for_status()
os.makedirs('imgur', exist_ok=True)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
imagePost = soup.select('.post')
if imagePost == []:
    print('Could not finy any images')
else:
    for i in range(len(imagePost)):
        img = imagePost[i].findAll('img')
        img_src = 'https:' + img[0]['src']
        print('Downloading %s...' % (img_src))
        res = requests.get(img_src, headers = {'User-agent': 'your bot 0.1'})
        res.raise_for_status()
        imageFile = open(os.path.join('imgur', os.path.basename(img_src)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    print('Done')

