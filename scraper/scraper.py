import requests
from bs4 import BeautifulSoup

url = 'https://example-blog.com'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = soup.find_all('h2')
    
    for title in titles:
        print(title.get_text())
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)