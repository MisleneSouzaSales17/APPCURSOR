def quadrados(n):
    return [i**2 for i in range(n)]
print(quadrados(5))

def soma(n):
    return sum(n)
print(soma([1, 2, 3, 4, 5]))

def media(n):
    return sum(n) / len(n)
print(media([1, 2, 3, 4, 5]))

def maior(n):
    return max(n)
print(maior([1, 2, 3, 4, 5]))

def menor(n):
    return min(n)
print(menor([1, 2, 3, 4, 5]))

def par(n):
    return [i for i in n if i % 2 == 0]
print(par([1, 2, 3, 4, 5]))

def impar(n):
    return [i for i in n if i % 2 != 0]
print(impar([1, 2, 3, 4, 5]))
