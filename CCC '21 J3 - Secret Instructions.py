d = ""

while True:
    n = input()

    if n == '99999':
        break

    c = int(n[0]) + int(n[1])
    a = n[2:]

    if c % 2 == 0 and c != 0:
        d = "right"
        print(f"right {a}")
    elif c == 0:
        print(f"{d} {a}")
    else:
        d = "left"
        print(f"left {a}")
