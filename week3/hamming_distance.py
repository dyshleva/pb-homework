def get_hdist(i: int, j: int) -> None:
    '''
    Get hamming distance of two numbers

    Args:
        i: First int for hamming distance
        j: Second int for hamming distance
    '''
    
    xorred_val = i^j
    # Make list of 1s/0s. A binary representation of i
    bin_rep = [(xorred_val >> x) & 1 for x in range(xorred_val.bit_length())]
    print(sum(bin_rep))

i, j = input().split()
get_hdist(int(i), int(j))
