import bs4
import requests
url = input('Enter link: ')
text = requests.get(url).text
soup = bs4.BeautifulSoup(text, 'html.parser')
ext = soup.find('h1').text.split('.')[-1] # Get the file extension
domain = 'https://spyderrock.com/' # This will probably need to be updated frequently
newurl = domain + url.split('/file/')[1] + '.' + ext
print(newurl)
