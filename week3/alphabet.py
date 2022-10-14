from string import ascii_uppercase

length = int(input())

letters = ascii_uppercase[0: length]

lines = []
pos = 0
height = 1
while pos < length:
    lines.append(''.join(letters[pos: pos + height]))
    pos += height
    height += 1

out = []
height = len(lines)
for i in range(height):
    justify = 2*height - 1 if i != height - 1 else 0
    out.append(" ".join(lines[i]).rjust(justify))

print("\n".join(out))
