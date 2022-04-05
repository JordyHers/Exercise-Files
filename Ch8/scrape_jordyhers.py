from bs4 import BeautifulSoup
import requests

url = 'http://jordyhers.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
print(soup)

# Here we request all the meta tags from the website
meta = soup.find_all('meta')


for each in meta:
    print(each)
