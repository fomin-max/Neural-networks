from pylab import *

def change(v, a, b):
    t = [[0 for j in range(a)] for i in range(b)]
    k = 0
    j = 0
    while k < b:
        i = 0
        while i < a:
            t[k][i] = v[j]
            j += 1
            i += 1
        k += 1
    return t

def hamming(a, b):
    i = 0
    r = 0
    while i < len(a):
        if a[i] != b[i]:
            r += 1
        i += 1
    return r

def product(w, y):
    z = []
    for i in range(len(w)):
        x = 0
        for j in range(len(y)):
            x = x + w[i][j]*y[j]
        if x >= 0:
            x = 1
        else:
            x = -1
        z.append(x)
    return z

# x = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
# x = [[ -1, -1, 1, -1],[ 1, -1, 1, -1],[ -1, 1, -1, -1]]
# x = [[-1,-1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1],[1,-1,-1,1,1,-1,-1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,1],[1,1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,1,1,1,1,1]]
# x = [[-1,-1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1],[1,-1,-1,1,1,-1,-1,1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,1]]
# m = int(input('Введите количество образцов: '))
# a = int(input('Введите ширину образца: '))
# b = int(input('Введите длину образца: '))
m = 2
a = 4
b = 5
f = open('example.txt')
t = []
for i in f:
    t.append(i.split(','))
    for k in range(len(t)):
        for j in range(len(t[k])):
            t[k][j] = int(t[k][j])
x = []
h = m
while h > 0:
    x.append(t[h])
    h -= 1
f.close()
n = len(x[0])
y = t.pop()
w = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        c = 0
        if i != j:
            for k in range(m):
                c = c + x[k][j]*x[k][i]
        w[i][j] = c
# y = [int(i) for i in input("Input y: ").split(' ')]
q = change(y, a, b)
plt.matshow(q)
plt.colorbar()
h = 0
while h < 5:
    z = product(w, y)
    r = hamming(z, y)
    h += 1
    if r == 0:
        z = change(z, a, b)
        print(z)
        plt.matshow(z)
        plt.colorbar()
        plt.show()
        exit()
    else:
        y = z
# 1,1,1,-1,-1,-1,1,1,1
# palka -1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1
# v = -1 -1 -1 1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 -1 1
# newv v = -1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 -1 -1
# print(change(v, 4,5))

# 1 1 1 1 -1 -1 -1 1 1 1 1 1 -1 -1 -1 1 -1 -1 1 1 цикл бесконечный
# -1 -1 -1 1 -1 -1 -1 1 1 1 1 1 -1 -1 -1 1 -1 -1 -1 1 ещё один
