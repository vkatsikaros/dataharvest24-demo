import requests
from bs4 import BeautifulSoup

url = 'https://vkatsikaros.github.io/dataharvest24-www.github.io/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    table = soup.find('table', id='target-table')  # Use id or class as necessary

    headers = []
    for th in table.find('thead').find_all('th'):
        headers.append(th.text.strip())

    rows = []
    for tr in table.find('tbody').find_all('tr'):
        cells = [td.text.strip() for td in tr.find_all('td')]
        rows.append(cells)

    print("Headers:", headers)
    for row in rows:
        print("Row:", row)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)