nome = input("digite o seu nome: ")
disciplina = input("digite a disciplina: ")
nota = float(input("dig:ite sua nota: "))
if nota>=0 and nota<=10:
    if nota >=6:
        print(f"o aluno esta aprovado na disciplina de {disciplina} com nota {nota}")
    if 5.5 <= nota < 6:
        print(f"o aluno esta aprovado na disciplina de {disciplina} com nota 6 ")
    if nota <5.5:
        print(f"o aluno esta reprovado na disciplina de {disciplina} com nota {nota}")
else:
    print("nota invalida")
