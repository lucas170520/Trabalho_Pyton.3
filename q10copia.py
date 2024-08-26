op = '1'
while op!= '0':
    print('''
    ---------------Calculadora.py------------------
    Escolha uma operação
    1-soma
    2-subtração
    3-multiplicação
    4-divisão
    5-elevar ao quadrado
    0-sair
    ''')
    op = input('op= ') 
    if op == '1': 
        n1 = int(input("digite um numero: "))
        n2 = int(input("digite outro numero: "))
        print(f"{n1} + {n2} = {n1+n2}")
    if op == '2':
        n1 = int(input("digite um numero: "))
        n2 = int(input("digite outro numero: "))
        print(f"{n1} - {n2} = {n1-n2}")
    if op == '3':
        n1 = int(input("digite um numero: "))
        n2 = int(input("digite outro numero: "))
        print(f"{n1} * {n2} = {n1*n2}")
    if op == '4':
        n1 = int(input("digite um numero: "))
        n2 = int(input("digite outro numero: "))
        print(f"{n1} / {n2} = {n1/n2}")
    if op == '5':
        n1 = int(input("digite um numero"))
        print(f"{n1} * {n1} = {n1*n1}")
    else:
        print("erro tente novamente")