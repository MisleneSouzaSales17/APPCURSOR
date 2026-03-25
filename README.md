# APPCURSOR

Um pequeno conjunto de scripts Python para praticar logica e manipular dados.

## Scripts incluidos

- `parse.py`
  - Leria um arquivo `dados.csv` com as colunas `col1` e `col2`.
  - Calcula media, mediana e desvio padrao para cada coluna.
  - Gera um grafico de dispersao (`col1` vs `col2`).

- `calculator.py`
  - Calculadora interativa no terminal.
  - Operacoes: `adicao`, `subtracao`, `multiplicacao`, `divisao`.
  - Encerra digitando `saida`.

- `FizzBuzz.py`
  - Implementacao classica do FizzBuzz para numeros de 1 a 50.

- `contador.py`
  - Pede o caminho de um arquivo de texto.
  - Conta palavras usando `re.findall(r"\\w+", texto)`.

- `test.py`
  - Exemplo simples: imprime "Hello World" e os numeros de 0 a 4.

## Requisitos

Alguns scripts usam bibliotecas externas:

- Para `parse.py`: `pandas` e `matplotlib`

Instalacao (se necessario):

```powershell
python -m pip install pandas matplotlib
```

## Como executar

Exemplos:

```powershell
python parse.py
python calculator.py
python FizzBuzz.py
python contador.py
python test.py
```

### `parse.py` (arquivo `dados.csv`)

Garanta que exista um `dados.csv` na mesma pasta do script, com cabecalho e colunas:

- `col1`
- `col2`

Exemplo de formato:

```csv
col1,col2
10,20
15,25
20,30
```

## Gerar um `.exe` (Windows) com PyInstaller

1. Instale o PyInstaller:

```powershell
python -m pip install pyinstaller
```

2. Gere o executavel (na pasta do projeto):

```powershell
pyinstaller --onefile parse.py
```

O arquivo final sera criado em `dist/`.

## Observacao

O `.exe` pode ficar grande dependendo das dependencias (ex.: `pandas`/`matplotlib`).