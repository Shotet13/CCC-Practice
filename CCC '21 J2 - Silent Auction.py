max_bid = -1
winner = ""

while True:
    name = input("Enter name: ")

    if name.lower() == 'stop':
        break

    current_bid = float(input("Enter bid: "))

    if max_bid < current_bid or (max_bid == current_bid and winner == ""):
        winner = name
        max_bid = current_bid

print(winner)
