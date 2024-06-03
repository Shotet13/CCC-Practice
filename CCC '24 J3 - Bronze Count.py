n = int(input())
scores = []
Nscores = []

for _ in range(n):
    score = int(input())
    scores.append(score)
    Nscores.append(score)

NFirst = max(scores)

First = max(scores)
scores.remove(First)

Second = max(scores)

while True:     
    if NFirst == Second:
        scores.remove(Second)
        Second = max(scores)
    else:
        break

Third = max(scores)

while True:     
    if NFirst == Third:
        scores.remove(Third)
        Third = max(scores)
    else:
        break

NSecond = max(scores)

while True:     
    if NSecond == Third:
        scores.remove(Third)
        Third = max(scores)
    else:
        break

Amount = scores.count(Third)

print(f"{Third} {Amount}")
