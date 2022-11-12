def ternary2binary(s: str):
    b = s[0]
    for i in range(1, len(s)):
        b = b + str(int(s[i])-int(b[-1]))
    return b