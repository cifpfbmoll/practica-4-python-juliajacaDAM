'''
Pida al usuario un importe en euros y diga si el cajero automático le puede dar 
dicho importe utilizando el mismo billete y el más grande  (recuerda que el billete
 puede ser de 500, 200, 100, 50, 20, 10 y 5€).
'''

importe = int(input('Escribe el saldo a retirar (Tiene que ser múltiplo de 5) ' ))

if importe % 5 != 0:
    print('El billete más pequeño es de 5 Euros. No podemos darte esa cantidad')
elif importe % 500 == 0:
    num_billetes = importe / 500
    print(f'El cajero te va a devolver {int(num_billetes)} billetes de 500 Euros ')
elif importe % 200 == 0:
    num_billetes = importe / 200
    print(f'El cajero te va a devolver {int(num_billetes)} billetes de 200 Euros ')
elif importe % 100 == 0:
    num_billetes = importe / 100
    print(f'El cajero te va a devolver {int(num_billetes)} billetes de 100 Euros ')
elif importe % 50 == 0:
    num_billetes = importe / 50
    print(f'El cajero te va a devolver {int(num_billetes)} billetes de 50 Euros ')
elif importe % 20 == 0:
    num_billetes = importe / 20
    print(f'El cajero te va a devolver {int(num_billetes)} billetes de 20 Euros ')
elif importe % 10 == 0:
    num_billetes = importe / 10
    print(f'El cajero te va a devolver {int(num_billetes)} billetes de 5 Euros ')
elif importe % 5 == 0:
    num_billetes = importe / 5
    print(f'El cajero te va a devolver {int(num_billetes)} billetes de 500 Euros ')