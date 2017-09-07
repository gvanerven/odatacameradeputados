import unittest
import odatacameradeputados


class GetInfoCDProposicoes(unittest.TestCase):
    def test_get_proposicoes_200OK(self):
        proposicoes = odatacameradeputados.get_proposicoes()
        self.assertTrue(proposicoes["status_code"] == 200)

    def test_get_proposicoes_not_none(self):
        proposicoes = odatacameradeputados.get_proposicoes()
        self.assertNotEqual(proposicoes, None)

    def test_get_proposicoes_not_empty(self):
        proposicoes = odatacameradeputados.get_proposicoes()
        self.assertTrue(len(proposicoes["proposicoes"]) > 0)

    def test_get_proposicoes_any_id(self):
        proposicoes = odatacameradeputados.get_proposicoes()
        self.assertTrue("id" in proposicoes["proposicoes"]["dados"][0]
                        and proposicoes["proposicoes"]["dados"][0]["id"] > 0)

    def test_get_proposicoes_first_id(self):
        # Preparing test
        proposicoes = odatacameradeputados.get_proposicoes()
        # retrieve the first id only
        id_proposicoes = proposicoes["proposicoes"]["dados"][1]["id"]
        proposicoes = odatacameradeputados.get_proposicoes(ids=id_proposicoes)
        self.assertTrue("id" in proposicoes["proposicoes"]["dados"][0]
                        and proposicoes["proposicoes"]["dados"][0]["id"] == id_proposicoes)

    def test_get_proposicoes_200OK_pg2(self):
        proposicoes = odatacameradeputados.get_proposicoes(pagina=2)
        self.assertTrue(proposicoes["status_code"] == 200)
        self.assertTrue(proposicoes["total_retornado"] > 0)

if __name__ == '__main__':
    unittest.main()
