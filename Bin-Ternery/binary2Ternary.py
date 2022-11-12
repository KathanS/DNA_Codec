def binaryToTernary(s: str):
    t = f'{s[0]}'
    for i in range(1,len(s)):
        t += str(int(s[i])+int(s[i-1]))
    return t