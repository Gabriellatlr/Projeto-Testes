def validar_notas(notas):
    if not notas:
        raise ValueError("Lista de notas vazia")

    for nota in notas:
        if not isinstance(nota, (int, float)):
            raise TypeError("Todas as notas devem ser numéricas")


def calcular_media(notas):
    validar_notas(notas)
    return sum(notas) / len(notas)


def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"

    if media >= 5:
        return "Recuperação"

    return "Reprovado"


def obter_maior_nota(notas):
    validar_notas(notas)
    return max(notas)