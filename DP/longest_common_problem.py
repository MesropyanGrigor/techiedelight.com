

def lcs(str_1, str_2):
    if not str_1 or not str_2:
        return 0
    elif str_1[-1] == str_2[-1]:
        return 1 + lcs(str_1[:-1], str_2[:-1])
    else:
        return max(lcs(str_1[:-1], str_2), lcs(str_1, str_2[:-1]))
    

if __name__ == '__main__':
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    print("Length of LCS is", lcs(S1, S2))