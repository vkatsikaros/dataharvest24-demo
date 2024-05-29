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
            thead = table.find('thead')
            if thead is not None:
                for th in thead.find_all('th'):
                    headers.append(th.text.strip())
            else:
                print("Thead not found in the table.")

            rows = []
            tbody = table.find('tbody')
            if tbody is not None:
                for tr in tbody.find_all('tr'):
                    row_data = []
                    for td in tr.find_all('td'):
                        # Find the <a> tag within the <td>
                        a_tag = td.find('a')
                        if a_tag is not None:
                            url = a_tag.get('href', None)  # Use get to avoid KeyError
                            text = a_tag.text.strip()
                            row_data.append((url, text))
                        else:
                            row_data.append((None, td.text.strip()))
                    rows.append(row_data)
            else:
                print("Tbody not found in the table.")

            if headers:
                print("Headers:", headers)
            else:
                print("No headers found.")
                
            if rows:
                for row in rows:
                    for cell in row:
                        url, text = cell
                        if url:
                            print(f"URL: {url}, Text: {text}")
                        else:
                            print(f"Text: {text}")
            else:
                print("No rows found.")
        else:
            print("Table not found within the div. Check the structure.")
    else:
        print("Div with id '_idItemTableForP' not found. Check the id.")
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)