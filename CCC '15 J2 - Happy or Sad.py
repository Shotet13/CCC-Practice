msg = input().strip()

happy = msg.count(":-)")
sad = msg.count(":-(")

if happy == 0 and sad == 0:
    print("none")
elif happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
elif happy == sad:
    print("unsure")
