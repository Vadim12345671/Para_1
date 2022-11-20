import requests
from bs4 import BeautifulSoup

resp = requests.get("https://bank.gov.ua/")

if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "value-full"})
    res = soup_list[1].find("small")
    print("Зараз курс доллора:", res.text, "$")