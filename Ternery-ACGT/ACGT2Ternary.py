first = {'A':'0', 'C':'1', 'G':'2'}
map = {
    'A': {'C':'0','G':'1','T':'2'},
    'C': {'G':'0','T':'1','A':'2'},
    'G': {'T':'0','A':'1','C':'2'},
    'T': {'A':'0','C':'1','G':'2'}
}

def TernaryToACGT(s: str):
    t = first[s[0]]
    for i in range(1, len(s)):
        t = t + map[s[i-1]][s[i]]
    return t

if __name__ == "__main__":
    print(TernaryToACGT("ACTCTG"))