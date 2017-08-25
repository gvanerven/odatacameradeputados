import unittest
import odatacameradeputados


class GetInfoCDProposicoes(unittest.TestCase):
    def test_get_proposicoes_simples(self):
        proposicoes = odatacameradeputados.get_proposicoes()
        self.assertNotEqual(proposicoes, None)
        self.assertTrue(len(proposicoes) > 0)
        self.assertTrue(proposicoes["status_code"] == 200)
        self.assertTrue(len(proposicoes["proposicoes"]) > 0)


if __name__ == '__main__':
    unittest.main()
