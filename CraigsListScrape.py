import requests
# https://requests.readthedocs.io/en/master/

from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Get list of offers
URL = 'https://sfbay.craigslist.org/search/cta?query=tesla'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='rows')
car_elems = results.find_all('li', class_='result-row')

# Parse each offer tile
for car_elem in car_elems:
    price_elem = car_elem.find('span', class_='result-price')
    url_elem = car_elem.find('a', class_="result-image gallery")['href']
    title_elem = car_elem.find('a', class_='result-title hdrlnk')

    print(title_elem.text.strip())
    print(url_elem)
    print(price_elem.text.strip())
    print()

# Get details of particular offer
CAR_URL = 'https://sfbay.craigslist.org/eby/cto/d/orinda-model-p90d/7136143103.html'
car_page = requests.get(CAR_URL)
car_soup = BeautifulSoup(car_page.content, 'html.parser')
attributes = car_soup.find_all('p', class_='attrgroup')

# Get attributes
for attribute in attributes:
    spans = attribute.find_all('span')
    for span in spans:
        text = span.text.strip()
        print(text)
        print(text.split(':'))
        print()

# Get offer description
posting_body = car_soup.find('section', {"id": "postingbody"})
print(posting_body.text)
