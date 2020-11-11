'''
Práctica 4. Ejercicio 3
Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, 
y pida los datos según que caso y muestre el resultado.
'''

figura_geometrica = input('''
¿Quieres calcular el área de un triángulo? -> Escribe T
¿O quieres calcular el área de un cuadrado? -> Esribe C
--------------------------------------------------
''')

if figura_geometrica.lower() == "t":
    print('Has escogido triángulo')
    base_triangulo = float(input('Introduce la base del triángulo '))
    altura_triangulo = float(input('Introduce la altura del triángulo '))
    area_triangulo = (base_triangulo *  altura_triangulo) / 2
    print(f''''El área de un triángulo con base {base_triangulo} 
    y altura {altura_triangulo} es {area_triangulo}''')
elif figura_geometrica.lower() == "c":
    print('Has escogido cuadrado')
    lado_cuadrado = float(input('Introduce el lado del cuadrado '))
    area_cuadrado = lado_cuadrado * lado_cuadrado
    print(f'El área de un cuadrado de lado {lado_cuadrado} es {area_cuadrado}')
else:
    print('¡No entiendo esa instrucción! Adiós')