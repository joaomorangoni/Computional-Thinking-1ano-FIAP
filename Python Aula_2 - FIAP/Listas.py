numeros = [1,2,3,4,5]

numeros.append(6)
print(numeros)

numeros2 = [7,8,9,10]
numeros.extend(numeros2)
print(numeros)

numeros.insert(4,10)
print(numeros)

numeros.append(1)
numeros.remove(1)
print(numeros)

removido = numeros.pop(6)
print(f"O numero removido da lista foi o: {removido}")
print(numeros)

print(numeros2)
numeros2.clear()
print(numeros2)

index = numeros.index(6)
print(index)

numero = 10
vezes = numeros.count(numero)
print(f"O numero {numero} se repete {vezes} vez(es)")

numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)

nova = numeros.copy()
print(nova)