N = int(input())
total = 0
largest = 0
strikes = 0
lastP = -1

for i in range(N):
    C = str(input())
    if C == 'S':
        total += 1
    if C == 'P':
        if strikes == 0:
            strikes = 1
            total += 1
            lastP = i
        else:
            total = i - lastP
            lastP = i

    if largest <= total:
        largest = total

print(largest)