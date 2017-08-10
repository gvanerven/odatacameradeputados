import requests
from . import URL_BASE_DEFAULT, HEADERS

def get_preposicoes():
    preposicoes = {}
    r = requests.get(URL_BASE_DEFAULT, headers=HEADERS)
    print(r)
    preposicoes["status_code"] = r.status_code
    return preposicoes
