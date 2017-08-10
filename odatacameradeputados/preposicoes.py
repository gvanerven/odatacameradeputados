import requests
from . import defaults

def get_preposicoes():
    preposicoes = {}
    r = requests.get(defaults.URL_BASE_DEFAULT, headers=defaults.HEADERS)
    print(r)
    preposicoes["status_code"] = r.status_code
    return preposicoes
