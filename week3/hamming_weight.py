def get_hweight(i: int) -> None:
    '''
    Get hamming weight of 5^i

    Args:
        i: int, to which power raise 5
    '''

    pow_five = 5**i
    # Make list of 1s/0s. A binary representation of 5^i
    bin_rep = [(pow_five >> i) & 1 for i in range(pow_five.bit_length())]
    bin_rep.reverse()
    bin_rep_sum = sum(bin_rep)
    print(f"Number { pow_five } is", end=" ")
    print(f"{ 'odious' if (bin_rep_sum % 2) else 'evil' } number.", end=" ")
    print(f"Its hamming weight is { bin_rep_sum }.")

get_hweight(int(input()))
