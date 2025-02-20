# N = int(input())
PC = input()
newPC = ''
num = 0

for i in range(len(PC)):
    if PC[i] == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'K' or 'L' or 'M' or 'N' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y' or 'Z':
        newPC += PC[i]
        print(f"ABC + {PC[i]} = {newPC}")
    if PC[i] == int:
        num += PC[i]
        print(f"123 + {PC[i]} = {newPC}")


# print(newPC)

# PC = str(input())

# for i in range(len(PC)):
#     print(i)
