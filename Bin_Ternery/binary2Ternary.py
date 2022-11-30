
from Pickle.extractData import *
def binary2ternary(secretCode):
    fileName1 = "ascii2bin_"
    fileName1 += secretCode+".pkl"
    s = extract_pickle(fileName1)
    t = f'{s[0]}'
    for i in range(1,len(s)):
        t += str(int(s[i])+int(s[i-1]))
    fileName2 = "binary2ternary"
    fileName2+=secretCode+".pkl"
    create_pickle(fileName2,t)
    return t
