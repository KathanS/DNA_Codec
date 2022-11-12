first = {'0':'A', '1':'C', '2':'G'}
map = {
    'A': {'0':'C','1':'G','2':'T'},
    'C': {'0':'G','1':'T','2':'A'},
    'G': {'0':'T','1':'A','2':'C'},
    'T': {'0':'A','1':'C','2':'G'}
}

def ternary2acgt(s: str):
    dna = first[s[0]]
    for i in range(1, len(s)):
        dna = dna + map[dna[-1]][s[i]]
    return dna
