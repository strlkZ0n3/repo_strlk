n = int(123237429)
l = []
s = str(n)
n = len(s)
c = 0
while c < n:
    l.append(s[c])
    c = c + 1
if '8' in l or '9' in l:
    print('No es octal, contiene 8 o 9')
else:
    print('Es octal')