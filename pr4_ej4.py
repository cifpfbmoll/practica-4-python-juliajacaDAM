'''
Práctica 4. Ejercicio 4
Pida al usuario tres números y un cuarto número, y compruebe si este último
es divisor de los tres números primeros.
'''

print('''
introduce cuatro números y te diré si el último es divisor de los otros tres.
--------------------------------------------------
''')

num_1 = int(input("Introduce el primer número \n"))
num_2 = int(input("Introduce el segundo número \n"))
num_3 = int(input("Introduce el tercer número \n"))
num_divisor = int(input("Introduce posible divisor \n"))

if (num_1 % num_divisor ==  0) and (num_2 % num_divisor == 0) and (num_3 % num_divisor == 0):
    print(f'Los números {num_1}, {num_2} y {num_3} son divisbles por {num_divisor}')
else:
    print(f'Los números {num_1}, {num_2} y {num_3} NO son divisbles por {num_divisor}')