# -*- coding: utf-8 -*-
def dec2bin():
        while True:
                try:
                        n = int(input('Ingrese un entero del sistema decimal: '))
                        break
                except ValueError:
                        print('\nError en el formato, ingrese un entero por favor')
        lista = []
        while n > 0:
                c = n//2
                r = n%2
                n = c
                lista.append(r)
        lista = lista[::-1]
        cl = len(lista)
        lis_var = ''
        q = int(0)
        while q < cl:
                x = lista[q]
                q = q+1
                lis_var = lis_var + str(x)
        print('\nEn hexadecimal es:'+2*'\n'+lis_var)
        input('Presione cualquier tecla para salir...')
dec2bin()