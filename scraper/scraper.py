import requests
from bs4 import BeautifulSoup
import csv
import io

url = 'https://vkatsikaros.github.io/dataharvest24-www.github.io/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find('div', id='_idItemTableForP')
    if div is not None:
        table = div.find('table')

        if table is not None:

            rows = []
            tbody = table.find('tbody')
            if tbody is not None:

                for tr in tbody.find_all('tr'):
                    row_data = []
                    for td in tr.find_all('td'):
                        # Find the second <a> tag within the <td>
                        a_tags = td.find_all('a')
                        if len(a_tags) >= 2:
                            second_a_tag = a_tags[1]
                            code_span = second_a_tag.find('span', class_='pspItemCateAndNo')
                            if code_span is not None:
                                code = code_span.text.strip().split(':')[-1].strip()
                                row_data.append(code)
                        else:
                            row_data.append('')
                    rows.append(row_data)
            else:
                print("Tbody not found in the table.")

            for row in rows:
                print("Code:", row[0])
        else:
            print("Table not found within the div. Check the structure.")
    else:
        print("Div with id '_idItemTableForP' not found. Check the id.")
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)