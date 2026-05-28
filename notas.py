def calcular_media(notas):
    if len(notas) == 0:
        raise ValueError("Lista de notas vazia")
    
    return sum(notas) / len(notas)


def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def maior_nota(notas):
    if len(notas) == 0:
        raise ValueError("Lista vazia")
    
    return max(notas)