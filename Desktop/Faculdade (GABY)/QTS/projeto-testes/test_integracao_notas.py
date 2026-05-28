import unittest
from notas import calcular_media, verificar_aprovacao, obter_maior_nota

class TestIntegracaoNotas(unittest.TestCase):
    def test_fluxo_aprovado(self):
        notas = [8, 9, 7]

        media = calcular_media(notas)
        resultado = verificar_aprovacao(media)

        self.assertEqual(media, 8)
        self.assertEqual(resultado, "Aprovado")

    def test_fluxo_recuperacao(self):
        notas = [5, 6, 5]

        media = calcular_media(notas)
        resultado = verificar_aprovacao(media)

        self.assertEqual(media, 5.333333333333333)
        self.assertEqual(resultado, "Recuperação")

    def test_fluxo_reprovado(self):
        notas = [2, 4, 3]

        media = calcular_media(notas)
        resultado = verificar_aprovacao(media)

        self.assertEqual(media, 3)
        self.assertEqual(resultado, "Reprovado")

    def test_fluxo_maior_nota_e_media(self):
        notas = [4, 9, 6]

        maior = obter_maior_nota(notas)
        media = calcular_media(notas)

        self.assertEqual(maior, 9)
        self.assertEqual(media, 6.333333333333333)

    def test_fluxo_lista_vazia(self):
        notas = []

        with self.assertRaises(ValueError):
            media = calcular_media(notas)
            verificar_aprovacao(media)


if __name__ == "__main__":
    unittest.main()