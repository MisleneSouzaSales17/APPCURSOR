# Programa para contar palavras em um arquivo de texto import re


def main() -> None:
    arquivo = input("Digite o caminho para o arquivo de texto: ")

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            texto = f.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return

    # Conta "palavras" como sequencias de caracteres alfanumericos (whitespace e pontuação separam).
    palavras = re.findall(r"\w+", texto)
    print(f"Total de palavras: {len(palavras)}")


if __name__ == "__main__":
    main()