A1 = int(input())
A2 = int(input())
A3 = int(input())

B1 = int(input())
B2 = int(input())
B3 = int(input())

if ((A1 * 3) + (A2 * 2) + (A3 * 1)) > ((B1 * 3) + (B2 * 2) + (B3 * 1)):
    print("A")
elif ((A1 * 3) + (A2 * 2) + (A3 * 1)) < ((B1 * 3) + (B2 * 2) + (B3 * 1)):
    print("B")
else:
    print("T")
