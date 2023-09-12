# Crie um programa que analise um texto fornecido pelo usuário. O programa deve contar o número de palavras (independentemente se há repetição ou não), 
# a quantidade de cada palavra e a quantidade de cada letra. Ignore maiúsculas e minúsculas ao contar letras (ou seja, transforme tudo para minúsculas).
# Faça o devido tratamento para pontuação e espaços ao contar palavras.

# O programa deve conter uma função chamada `analisar_texto` que recebe o texto como parâmetro e retorna a contagem de palavras, 
#a frequência de palavras e a frequência de letras. A função deve ser devidamente documentada.

# Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve imprimir:

# ```
# Contagem de palavras: 8
# Frequência de palavras: Counter({'Olá': 2, 'mundo': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste': 1, 'novamente': 1})
# Frequência de letras: Counter({' ': 7, 'e': 6, 'o': 4, 't': 4, 'm': 3, 'n': 3, 'l': 2, 'á': 2, 'u': 2, 's': 2, 'd': 1, 'é': 1, 'v': 1, 'a': 1})
# ```

import string
print(string.punctuation)
print(string.ascii_letters)
print('-'*20)
from collections import Counter
print(Counter(['a','b','a','c','b','a']))
print(Counter('abacba'))
print('-'*20)
print('-'*20)
#1- solucao

def analisar_texto(texto):
    palavras = texto.split()
    contagem_palavras = len(palavras)
    frequencia_palavras = Counter(palavras)
    frequencia_letras = Counter(texto)
    return contagem_palavras, frequencia_palavras, frequencia_letras

texto = "Olá mundo! Este é um teste. Olá novamente."
contagem_palavras, frequencia_palavras, frequencia_letras =  analisar_texto(texto)
print(f"Contagem de palavras: {contagem_palavras}")
print(f"Frequencia de palavras: {frequencia_palavras}")
print(f"Frequencia de letras: {frequencia_letras}")
print('-'*20)
print('-'*20)
vogais = "aeiou"
numeros = "12345"
remover = "a"
guia_troca = str.maketrans(vogais, numeros, remover)
print(guia_troca)
letras_minusculas = string.ascii_lowercase
print(letras_minusculas.translate(guia_troca))

print('#'*20)
print('#'*20)

def analisar_texto(texto):
    """Analisa o texto fornecido e calcula a contagem de palavras,
    frequencia de palavras e frequencia de letras

    Args:
        texto (_str_): _texto a ser analisado_

    Returns:
        _tupla_: _contagem de palavras, frequencia de palavras, frequencia de letras_
    """
    tratamento = str.maketrans("","",string.punctuation)
    texto_tratado = texto.translate(tratamento)
    palavras = texto_tratado.split()
    contagem_palavras = len(palavras)
    frequencia_palavras = Counter(palavras)
    frequencia_letras = Counter(texto_tratado.lower())
    return contagem_palavras, frequencia_palavras, frequencia_letras

texto = "Olá mundo! Este é um teste. Olá novamente."
contagem_palavras, frequencia_palavras, frequencia_letras =  analisar_texto(texto)
print(f"Contagem de palavras: {contagem_palavras}")
print(f"Frequencia de palavras: {frequencia_palavras}")
print(f"Frequencia de letras: {frequencia_letras}")