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
    if op == '1' or '2' or '3' or '4' or '5' or '0':
        if op == '1': 
            n1 = int(input("digite um numero: "))
            n2 = int(input("digite outro numero: "))
            print(f"{n1} + {n2} = {n1+n2}")
        elif op == '2':
            n1 = int(input("digite um numero: "))
            n2 = int(input("digite outro numero: "))
            print(f"{n1} - {n2} = {n1-n2}")
        elif op == '3':
            n1 = int(input("digite um numero: "))
            n2 = int(input("digite outro numero: "))
            print(f"{n1} * {n2} = {n1*n2}")
        elif op == '4':
            n1 = int(input("digite um numero: "))
            n2 = int(input("digite outro numero: "))
            print(f"{n1} / {n2} = {n1/n2}")
        elif op == '5':
            n1 = int(input("digite um numero"))
            print(f"{n1} * {n1} = {n1*n1}")
        elif op == '0':
            print("Tchau")
        else:
            print('erro tente novamente')