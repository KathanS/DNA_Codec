from Pickle.extractData import *
first = {'A':'0', 'C':'1', 'G':'2'}
map = {
    'A': {'C':'0','G':'1','T':'2'},
    'C': {'G':'0','T':'1','A':'2'},
    'G': {'T':'0','A':'1','C':'2'},
    'T': {'A':'0','C':'1','G':'2'}
}

def acgt2ternary(secretCode):
    t = first[s[0]]
    fileName1 = "ternary2acgt"
    filName1+=secretCode+".pkl"
    s=extract_pickle(fileName1)
    for i in range(1, len(s)):
        t = t + map[s[i-1]][s[i]]
    fileName2 = "acgt2ternary"
    fileName2+=secretCode+".pkl"
    create_pickle(fileName2,t)
    
    return t
