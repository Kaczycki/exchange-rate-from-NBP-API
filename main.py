import json
import requests
from time import localtime

czas = localtime()
today_formatted = f'{czas.tm_year}-{czas.tm_mon}-{czas.tm_mday}'

currencycode = 'EUR'
print('Archiwum kursów średnich NBP')
while (True):
    datequoted = input('wprowadź datę w formacie YYYY-MM-DD:')
    try:
        with open('kurs.json', mode = 'w') as my_file:
            response = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/"+datequoted)
            lista = response.json()
            # print(lista[0])
            my_file.write(json.dumps(lista, indent = 2))
            # print(my_file.readline())
            # print(my_file.readline())
            # print(lista)
            break
    except:
        print('zły format danych')


with open('kurs.json', mode = 'r') as my_file:
    content = json.load(my_file)
    items = dict(content[0])
    print('tabela ', items['table'], ' numer ', items['no'], ' -->kursy z dnia ', items['effectiveDate'])
    for kurs in items['rates']:
        print(kurs['currency'], ' (', kurs['code'], '):')
        print(kurs['mid'])
