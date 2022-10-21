"""
Read-write filte submission
"""

from typing import List

from urllib.request import urlopen

def read_input_file(url: str, number: int) -> List[List[str]]:
    """
    Return list of strings lists from url

    Args:
        url: the url
        number: the amount of students
    Returns:
        the list rep of a student

    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder\
/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder\
/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'],\
 ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    lst = []
    with urlopen(url) as file:
        for line in file:
            if not line.decode('utf-8').startswith('#') and\
                not line.decode('utf-8').startswith('—'):
                lst.append(line.strip().decode('utf-8'))

    lst = list(filter(lambda x: 'До' in x or 'Середній' in x, lst))
    res = []
    for i in range(0, len(lst), 2):
        if not lst[i].startswith('С'):
            student_formatted = [
                    lst[i].split()[0],
            f"{lst[i].split()[1]} {lst[i].split()[2]} {lst[i].split()[3]}",
                    '+',
                    lst[i].split()[6],
                    lst[i+1].split()[-1]
                ]
            res.append(student_formatted)

    return res[:number]

def write_csv_file(url: str):
    """
    Write the file to total.txt

    Args:
        url: the url
    Returns:
        None
    >>> write_csv_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder\
/total.txt')

    """
    with open("total.csv", 'w', encoding='utf-8') as outfile:
        outfile.write("№,ПІБ,Д,Заг.бал,С.б.док.осв.")
        for line in read_input_file(url,1000):
            outfile.write(','.join(line))
