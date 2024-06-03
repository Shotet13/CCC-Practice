d = int(input())

while True:
    y = int(input())
    if d > y:
        d += y
    elif d <= y:
        break

print(d)
