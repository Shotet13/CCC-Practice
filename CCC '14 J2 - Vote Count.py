v = int(input())
votes = input().strip()

a_votes = votes.count("A")
b_votes = votes.count("B")

if a_votes > b_votes:
    print("A")
elif b_votes > a_votes:
    print("B")
else:
    print("Tie")
