import unittest
from notas import calcular_media, verificar_aprovacao, maior_nota

class TestNotas(unittest.TestCase):

    def test_calcular_media_normal(self):
        self.assertEqual(calcular_media([7, 8, 9]), 8)

    def test_calcular_media_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])

    def test_aprovado(self):
        self.assertEqual(verificar_aprovacao(7), "Aprovado")

    def test_recuperacao(self):
        self.assertEqual(verificar_aprovacao(5.5), "Recuperação")

    def test_reprovado(self):
        self.assertEqual(verificar_aprovacao(3), "Reprovado")

    def test_maior_nota(self):
        self.assertEqual(maior_nota([5, 10, 7]), 10)

    def test_maior_nota_vazia(self):
        with self.assertRaises(ValueError):
            maior_nota([])


if __name__ == "__main__":
    unittest.main()