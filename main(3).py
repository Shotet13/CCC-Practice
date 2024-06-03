boxes = int(input("Boxes delivered: "))
collisions = int(input("Collisions occured:"))

points = boxes*50 - collisions*10

if boxes > collisions:
    points += 500

print(points)