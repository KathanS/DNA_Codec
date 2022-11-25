
from Pickle.extractData import *
def ternary2binary(secretCode):
    fileName1 = "acgt2ternary"
    fileName1+=secretCode+".pkl"
    s=extract_pickle(fileName1)
    b = s[0]
    for i in range(1, len(s)):
        b = b + str(int(s[i])-int(b[-1]))
    fileName2 = "ternary2binary"
    fileName2+=secretCode+".pkl"
    create_pickle(fileName2,b)
    return b