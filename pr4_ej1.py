'''
Práctica 4. Ejercicio 1
Pida al usuario 5 números y diga cuál es el mayor y cuál el menor
'''
print('''
De los 5 números que introduzcas, yo te diré cuál es el mayor y cual el menor
--------------------------------------------------
''')
num_1 = float(input("Introduce el primer número \n"))
num_2 = float(input("Introduce el segundo número \n"))
num_3 = float(input("Introduce el tercer número \n"))
num_4 = float(input("Introduce el cuarto número \n"))
num_5 = float(input("Introduce el quinto número \n"))

lista_numeros = list() # también se puede lista_numeros = []

lista_numeros.append(num_1)
lista_numeros.append(num_2)
lista_numeros.append(num_3)
lista_numeros.append(num_4)
lista_numeros.append(num_5)
lista_numeros.sort()

print(f'''El menor número de los que has introducido es {lista_numeros[0]} 
y el mayor es {lista_numeros[-1]}''')

