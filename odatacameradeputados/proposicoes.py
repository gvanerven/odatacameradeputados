import requests
from . import defaults


def get_proposicoes(debug=False):
    proposicoes = {}
    r = requests.get(defaults.URL_BASE_PROPOSICOES.format(""), headers=defaults.HEADERS)
    if debug:
        print(r.content)
    proposicoes["status_code"] = r.status_code
    proposicoes["proposicoes"] = r.json()
    if debug:
        print(proposicoes)
    return proposicoes
