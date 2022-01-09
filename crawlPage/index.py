import requests
import time
import json
import random
from bs4 import BeautifulSoup

def processDataOnePage(index):
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    url = 'https://www.abuseipdb.com/sitemap?page='+str(index)
    x = requests.get(url,headers=header)
    soup = BeautifulSoup(x.text, 'html.parser')
    tablesIP = soup.find_all('div', class_='row')
    colmd4 = soup.find_all('div', class_='col-md-4')
    if colmd4:
        listTagA = [] 
        #print(colmd4[0].find_all('a'))
        for i in colmd4:
            listTagA.append(i.find_all('a'))
        listIP = []
        for tagA in listTagA:
            for i in tagA:
                listIP.append(i.contents[0])
        #print(listIP)    
        return listIP
    return "null"

def main():
    full_List_Ip = []
    numberPage = 1 
    res = "not null"
    while res != "null":
        print("Getting data Page: " + str(numberPage))
        res = processDataOnePage(numberPage)
        full_List_Ip.extend(res)
        numberPage = numberPage + 1
        antiblock = random.randint(0, 9)
        time.sleep(antiblock/10)
        print("Sleep: " + str(antiblock/10))
    numberPage = numberPage - 1
    print("Done getting all : " + str(numberPage) + " pages.")
    print(full_List_Ip)

if __name__ == "__main__":
    main()