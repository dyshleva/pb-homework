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

def make_gray_code(bin_rep: str) -> str:
    '''
    Make a gray code of a binary representation

    Args:
        bin_rep: binary representation of an integer
    '''
    prefix, final_bin_rep = undo_zeros(bin_rep)
    decimal_rep = int(final_bin_rep, 2) 
    gray_code = decimal_rep ^ (decimal_rep << 1)
    out = (str(bin(gray_code))[2:])[:len(final_bin_rep)]
    return prefix + out

print(make_gray_code(input()))
