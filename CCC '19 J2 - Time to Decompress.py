L = int(input())

for _ in range(L):
    line = input().split()
    N = int(line[0])
    character = line[1]
    print(character * int(N))
