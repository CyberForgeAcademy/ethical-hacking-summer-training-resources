import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://cyberforge.academy'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the response with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all h1 tags where class is wp-block-heading
    heading = soup.find('h2', class_='wp-block-heading').get_text()
    print("Heading is: ", heading)
    print("\n--------------------------------------\n")
    
    # Find all h3 tags
    subHeadings = soup.find_all('h3')
    for subHeading in subHeadings:
        print(subHeading.get_text())
    
    print("\n--------------------------------------\n")
        
    # Find all div contents where class is wp-container-core-columns-is-layout-2
    divContents = soup.find(class_='wp-container-core-columns-is-layout-2')
    for div in divContents:
        print(div.get_text())
    
    print("\n--------------------------------------\n")
        
    # Find all links
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
