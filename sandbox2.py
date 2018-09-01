while True:
    try:
        n = int(input('Ingrese un entero del sistema decimal: '))
        l = []
        s = str(n)
        t = len(s)
        c = 0
        while c < t:
            l.append(s[c])
            c = c + 1
        if '8' in l or '9' in l:
            print('No es octal, contiene 8 o 9')
        else:
            print('Todo en orden')
        break
    except ValueError:
        print('\nError en el formato, ingrese un entero por favor')
print('Sigue programa')