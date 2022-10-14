height = int(input())

for i in range(1, height+1):
    if i<3 or i==height:
        print("*"*i)
    else:
        print("*" + " "*(i-2) + "*")
