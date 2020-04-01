# -*- coding: utf-8 -*-

def rupee_euro(rupees):
    euros = round((rupees / 77.75), 2)
    print(euros)

def euro_rupee(euros):
    rupees = round((euros * 77.75), 2)
    print(rupees)


def run():
    print('C A L C U L A D O R A   D E   D I V I S A S')
    print('Convierte rupias hindúes a euros.')
    print('')

    tipo = int(input("Indica el tipo de cambio: \n 1. euro-rupia \n 2. rupia-euro \n"))

    if tipo == 1:
        euros = float(input("Ingresa la cantidad de euros que quieres convertir a rupias: "))
        euro_rupee(euros)
    elif tipo == 2:
        rupees = float(input("Ingresa la cantidad de rupias que quieres convertir a euros: "))
        rupee_euro(rupees)
    else:
        print("Tipo inválido")


if __name__ == '__main__':
    run()
