import requests
import json
from bs4 import BeautifulSoup

def getDataIpNew():
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    x = requests.get('https://www.abuseipdb.com/',headers=header)
    soup = BeautifulSoup(x.text, 'html.parser')
    tablesIP = soup.find_all('div', class_='col-md-3 col-xs-6')
    jsonListIp = []
    for row in tablesIP:
        dataIP = row.find('a').contents
        countryIP = row.find('img').get('title')
        jsonListIp.append({"CountryIP":countryIP,"IP":dataIP[0]})
        #print('CountryIP: {} - IP: {}'.format(countryIP, dataIP[0]))
    return json.dumps(jsonListIp)

print(getDataIpNew())