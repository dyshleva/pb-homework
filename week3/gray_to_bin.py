def undo_zeros(s: str) -> (str, str):
    '''
    Remove zeros at the beginning of binary representation

    Args:
        s: string to be modified
    '''
    new_out = ""
    lst = ""
    found_one = False
    for ch in s:
        if not found_one and ch=='0':
            lst += ch
        elif ch=='1':
            found_one = True
            new_out += ch
        else:
            new_out += ch
    return (lst, new_out)

def undo_gray_code(gray_rep: str) -> str:
    '''
    Make a binary code of a gray representation

    Args:
        gray_rep: binary representation of an integer
    '''
    prefix, gray_code = undo_zeros(gray_rep)
    bin_rep = gray_code[0]
    for i, ch in enumerate(gray_code[1:]):
        bin_rep += str(int(ch) ^ int(bin_rep[i]))

    return prefix + bin_rep

print(undo_gray_code(input()))
