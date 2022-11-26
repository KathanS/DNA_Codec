def ascii_2_binary(string):
    out = ""
    for i in range(len(string)):
        t = ""
        temp = ord(string[i])
        while temp:
            t += str(temp%2)
            temp = int(temp/2)
        
        need = 8 - len(t)%8
        t = t[::-1]
        if(need !=0):
            for j in range(0,need):
                t = '0' + t
        out += t
    return out
