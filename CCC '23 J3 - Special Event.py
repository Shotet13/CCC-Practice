n = int(input())

mon = 0
tue = 0
wed = 0
thu = 0
fri = 0

c = 0

for _ in range(n):
    s = input().strip()

    mon += 1 if s[0] == 'Y' else 0
    tue += 1 if s[1] == 'Y' else 0
    wed += 1 if s[2] == 'Y' else 0
    thu += 1 if s[3] == 'Y' else 0
    fri += 1 if s[4] == 'Y' else 0

max_count = max(mon, tue, wed, thu, fri)

max_days = []

if max_count == mon:
    max_days.append("1")
if max_count == tue:
    max_days.append("2")
if max_count == wed:
    max_days.append("3")
if max_count == thu:
    max_days.append("4")
if max_count == fri:
    max_days.append("5")

if len(max_days) == 1:
    print(max_days[0])
else:
    print(",".join(max_days))
