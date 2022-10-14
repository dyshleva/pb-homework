games = []

i = str(input())
while i:
    games.append(i)
    i = str(input())

for game in games:
    if game[0] == game[1]:
        print("False | False")
    elif game in "SPRS":
        print(True)
    else:
        print(False)
