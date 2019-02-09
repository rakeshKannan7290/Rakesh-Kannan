from bs4 import BeautifulSoup
import requests
import csv

url = input()

response = requests.get(url)

if response.status_code==200:
    soup=BeautifulSoup(response.text,'lxml')
    cn = soup.getText().lower()
    wd = input()
    tn = cn.split()
    with open("Test.csv", "w", newline='') as f:
            w = csv.writer(f)
            for x in tn:
                ex = x.encode('utf8')
                w.writerow([ex])

    f1 = open("Test.csv", "r")
    rd = f1.read()
    f1.close()    
    print(rd.count(wd))

else:
    print("Invalid URL")
