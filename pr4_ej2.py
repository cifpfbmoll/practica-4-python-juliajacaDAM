'''
Práctica 4. Ejercicio 2
Pida al usuario 5 números y diga si estos estaban en orden decreciente,
creciente o desordenados.
'''
print('''
introduce cinco número y te diré si están en orde creciente, decreciente,
o desordenados.
--------------------------------------------------
''')

num_1 = float(input("Introduce el primer número \n"))
num_2 = float(input("Introduce el segundo número \n"))
num_3 = float(input("Introduce el tercer número \n"))
num_4 = float(input("Introduce el cuarto número \n"))
num_5 = float(input("Introduce el quinto número \n"))

lista_numeros = []

lista_numeros.append(num_1)
lista_numeros.append(num_2)
lista_numeros.append(num_3)
lista_numeros.append(num_4)
lista_numeros.append(num_5)

if lista_numeros == sorted(lista_numeros):
    print(f'{lista_numeros} es una lista ordenada creciente')
elif lista_numeros == sorted(lista_numeros, reverse=True):
    print(f'{lista_numeros} es una lista ordenada decreciente')
else:
    print(f'{lista_numeros} es una lista desordenada')
