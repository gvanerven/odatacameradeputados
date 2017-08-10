import unittest
import odatacameradeputados


class GetInfoCDPreposicoes(unittest.TestCase):
    def test_get_preposicoes_simples(self):
        preposicoes = odatacameradeputados.get_preposicoes()
        self.assertNotEqual(preposicoes, None)
        self.assertTrue(len(preposicoes) > 0)


if __name__ == '__main__':
    unittest.main()
