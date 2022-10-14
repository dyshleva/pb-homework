lst = []
for i in range(5):
    lst.append(int(input()))

grade_mins = [(90,"A"), (82, "B"), (75, "C"), (67, "D"), (60, "E"), (0, "F")]
def get_grade(grade):
    for i in grade_mins:
        if grade >= i[0]:
            return i[1]
    return None

for i in lst:
    if i > 100 or i < 0:
        print(None)
        exit()
avg = round(sum(lst)/len(lst), 2)
avg = int(avg) if avg == int(avg) else avg
print(f"Average grade = {avg} -> {get_grade(avg)}")

