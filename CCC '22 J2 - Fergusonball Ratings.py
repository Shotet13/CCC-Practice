n = int(input())
players = 0
num = n

for _ in range(n):
    score = int(input())
    fouls = int(input())
    total = (score * 5) + (fouls * -3)
    if total > 40:
        players += 1
        num -= 1

if num == 0:
    print(f"{players}+")
else:
    print(players)
