n = int(input())
x = []
y = []

for _ in range(n):
    h = input()
    x1, y1 = map(int, h.split(','))
    x.append(x1)
    y.append(y1)

min_x = int(min(x)) - 1
max_x = int(max(x)) + 1
min_y = int(min(y)) - 1
max_y = int(max(y)) + 1

print(f"{min_x},{min_y}\n{max_x},{max_y}")
