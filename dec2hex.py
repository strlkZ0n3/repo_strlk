# -*- coding: utf-8 -*-
def dec2hexa():
        while True:
                try:
                        n = int(input('Ingrese un entero del sistema decimal: '))
                        break
                except ValueError:
                        print('\nError en el formato, ingrese un entero por favor')
        lista = []
        while n > 0:
                c = n//16
                r = n%16
                n = c
                lista.append(r)
        lista = lista[::-1]
        cl = len(lista)
        lis_var = ''
        q = int(0)
        while q < cl:
                x = lista[q]
                q = q+1
                if x == 10:
                        x = 'A'
                elif x == 11:
                        x = 'B'
                elif x == 12:
                        x = 'C'
                elif x == 13:
                        x = 'D'
                elif x == 14:
                        x = 'E'
                elif x == 15:
                        x = 'F'
                else:
                        pass
                lis_var = lis_var + str(x)
        print('\nEn hexadecimal es:'+2*'\n'+lis_var)
        input('Presione cualquier tecla para salir...')
dec2hexa()