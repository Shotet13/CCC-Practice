num = int(input())

for _ in range(num):
    num = int(input())
    while num >=10:
        num = sum(int(digit) for digit in str(num))
    print(num)
