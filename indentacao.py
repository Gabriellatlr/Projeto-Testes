#código funcionando
notas = [7, 8, 5, 9]
soma = 0

for n in notas:
    soma = soma + n

media = soma / len(notas)

if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

print("Média:", media)