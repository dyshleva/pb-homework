series_length = int(input())

j = 2

for i in range(series_length):
    print(f"{j-1}/{j}", end = "")
    j += 2
    if i != series_length - 1:
        print(f" {'+' if (i % 2) != 0 else '-'}", end=" ")

print()

