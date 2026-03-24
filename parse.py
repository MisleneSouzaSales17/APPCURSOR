import pandas as pd  # pyright: ignore[reportMissingImports]
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingImports]

df = pd.read_csv("dados.csv")

def main():
    # 1. Ler o CSV
    # Exemplo de CSV: dados.csv
    # col1,col2
    # 10,20
    # 15,25
    # 20,30
    # 25,35
    # 30,40
    df = pd.read_csv("dados.csv")

    # 2. Calcular estatísticas simples
    print("Estatísticas da Coluna 1:")
    print("Média:", df['col1'].mean())
    print("Mediana:", df['col1'].median())
    print("Desvio padrão:", df['col1'].std())

    print("\nEstatísticas da Coluna 2:")
    print("Média:", df['col2'].mean())
    print("Mediana:", df['col2'].median())
    print("Desvio padrão:", df['col2'].std())

    # 3. Gerar gráfico de dispersão
    plt.scatter(df['col1'], df['col2'])
    plt.xlabel("Coluna 1")
    plt.ylabel("Coluna 2")
    plt.title("Gráfico de dispersão: col1 vs col2")
    plt.show()

if __name__ == "__main__":
    main()