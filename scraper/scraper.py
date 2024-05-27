import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://vkatsikaros.github.io/dataharvest24-www.github.io/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
   # Parse the HTML content of the page
   soup = BeautifulSoup(response.content, 'html.parser')
  
   # Find all the article titles on the page
   # This example assumes that the article titles are contained in <h2> tags
   titles = soup.find_all('h2')
  
   # Loop through the titles and print them out
   for title in titles:
       print(title.get_text())
else:
   print('Failed to retrieve the webpage. Status code:', response.status_code)