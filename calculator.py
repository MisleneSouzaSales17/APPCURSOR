def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    return a / b

# Dicionário de operações
operacoes = {
    "adição": adicionar,
    "subtração": subtrair,
    "multiplicação": multiplicar,
    "divisão": dividir
}

def main():
    while True:
        operacao = input("Digite a operação (adição, subtração, multiplicação, divisão) ou 'saída' para encerrar: ").strip().lower()
        
        if operacao == "saída":
            print("Encerrando a calculadora. Até mais!")
            break
        
        if operacao not in operacoes:
            print("Operação inválida. Tente novamente.")
            continue
        
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue
        
        resultado = operacoes[operacao](num1, num2)
        print(f"Resultado da {operacao}: {resultado}")

if __name__ == "__main__":
    main()