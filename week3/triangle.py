start = int(input())
height = int(input())

output = "\n".join(
    [
        " ".join(map(str, range(start, start + (height - i))))
        for i in range(height)
    ]
)

print(output)
