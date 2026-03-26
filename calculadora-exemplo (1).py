

def somarNum(x, y):
    soma = x + y
    return soma

def subtrairNum(x, y):
    subtracao = x - y
    return subtracao

def multiplicarNum(x, y):
    mult = x * y
    return mult

def dividirNum(x, y):
    if y == 0:
        print("Erro: Divisão por zero.")
        return None
    div = x / y
    return div

def calculaNum():
    print("Calculadora")
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))

    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao == "+":
        resultado = somarNum(x, y)
    elif operacao == "-":
        resultado = subtrairNum(x, y)
    elif operacao == "*":
        resultado = multiplicarNum(x, y)
    elif operacao == "/":
        resultado = dividirNum(x, y)
    else:
        print("Operação inválida")
        return

    print("Resultado:", resultado)

# Chamando a função principal para executar a calculadora
calculaNum()