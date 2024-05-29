import requests
from bs4 import BeautifulSoup

url = 'https://vkatsikaros.github.io/dataharvest24-www.github.io/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find('div', id='_idItemTableForP')

    if div is not None:
        table = div.find('table')

        if table is not None:
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
            print("Table not found within the div. Check the structure.")
    else:
        print("Div with id '_idItemTableForP' not found. Check the id.")
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)