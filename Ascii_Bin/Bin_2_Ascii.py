from Pickle.extractData import *

def binary_2_ascii(secretCode):
    fileName1 = "ternary2binary"
    fileName1+=secretCode+".pkl"
    string = extract_pickle(fileName1)
    out = ""
    t = 0
    k = 7
    for i in range(len(string)):
        t = t + (ord(string[i])-ord('0')) * int(pow(2,k))
        if (i+1)%8==0:
            out += chr(t)
            k = 8
            t = 0
        k = k-1
        
    fileName2 = "binary2ascii"
    fileName2+=secretCode+".pkl"
    create_pickle(fileName2,out)
    return out
