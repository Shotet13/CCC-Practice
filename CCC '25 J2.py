D = int(input())
E = int(input())

for i in range(E):
    q = input()
    Q = int(input())
    if q == '+':
        D += Q
    if q == '-':
        D -= Q

print(D)
