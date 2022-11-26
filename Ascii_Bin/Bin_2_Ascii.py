def binary_2_ascii(string):
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
    return out
