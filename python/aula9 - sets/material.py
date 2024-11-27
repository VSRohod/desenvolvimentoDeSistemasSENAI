"""
SETS - CONJUNTOS
https://brasilescola.uol.com.br/matematica/conjunto.htm

- 1 º NÃO TEM INDICE (NÃO GARANTE ORDEM)
- 2 º NÃO ACEITA CONTEUDO REPETIDO
"""

# CRIANDO SET
a = set('VICTOR')
teste = ['OI','OI','OI']
print(a)
print(set(teste))

b = {'Victor',1,2,3,4,5,6}
print(b)

c = set()
print(c , type(c))

# metodos uteis 
conjunto = set()
conjunto.add(10)
conjunto.add(8)

conjunto.update((3,5,6,'BOM DIA'))

conjunto.discard('BOM DIA')

print("*"*20)
print(conjunto)

# UNIÃO (union) - une dois
# INTERSECÇÃO (instersection) - comum nos dois
# DIFERENÇA - item presentes apenas em um conjunto
conjuntoA = {1,2,3,4,5}
conjuntoB = {5,6,7,8,9}
conjuntoC = set()

# | union
conjuntoC = conjuntoA | conjuntoB 
# & intersection
conjuntoC = conjuntoA & conjuntoB 
# - diference = diferença em relação ao
# conjunto da esquerda
conjuntoC = conjuntoB - conjuntoA
# ^ difence = diferença em relação a ambos os conjuntos
conjuntoC = conjuntoA ^ conjuntoB

for elemento in conjuntoC:
    print(elemento)

print(conjuntoC)