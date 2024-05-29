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
                            row_data.append(url)
                            row_data.append(text)
                        else:
                            row_data.append(td.text.strip())
                    rows.append(row_data)
            else:
                print("Tbody not found in the table.")

            output = io.StringIO()
            csv_writer = csv.writer(output)
            
            if headers:
                csv_writer.writerow(headers)
                
            if rows:
                for row in rows:
                    csv_writer.writerow(row)

            csv_content = output.getvalue()
            print(csv_content)
        else:
            print("Table not found within the div. Check the structure.")
    else:
        print("Div with id '_idItemTableForP' not found. Check the id.")
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)