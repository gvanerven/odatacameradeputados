import requests
from . import defaults


def get_proposicoes(debug=False, url=None, ids=None, pagina="1", ordem="ASC", ordenarPor="id"):
    #?id=12665&id=12666&ordem=ASC&ordenarPor=id
    proposicoes = {}
    options = "?ordem=" + ordem + "&ordenarPor=" + ordenarPor + "&pagina=" + str(pagina)
    if url == None:
        url = defaults.URL_BASE_PROPOSICOES

    if ids != None:
        if isinstance(ids, list):
            for id in ids:
                options = options + "&id=" + str(id)
        else:
            options = options + "&id=" + str(ids)

    r = requests.get(url.format(options), headers=defaults.HEADERS)
    if debug:
        print(r.content)

    proposicoes["proposicoes"] = r.json()
    if "dados" in proposicoes["proposicoes"]:
        proposicoes["total_retornado"] = len(proposicoes["proposicoes"]["dados"])
    else:
        proposicoes["total_retornado"] = -1

    proposicoes["link"] = r.headers["link"]
    proposicoes["total_count"] = r.headers["x-total-count"]
    proposicoes["status_code"] = r.status_code

    if debug:
        print(proposicoes)
    return proposicoes
