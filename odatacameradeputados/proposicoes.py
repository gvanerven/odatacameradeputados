import requests
import json
from . import defaults

def get_proposicoes():
    proposicoes = {}
    r = requests.get(defaults.URL_BASE_PROPOSICOES.format(""), headers=defaults.HEADERS)
    print(r.content)
    proposicoes["status_code"] = r.status_code
    proposicoes["proposicoes"] = r.content["dados"]
    return proposicoes
