def isSubsequence(s, t):
    len_s = len(s)
    if len_s == 0:
        return True
    i = 0
    for j in t:
        if len_s == i:
            return True
        if j == s[i]:
            i += 1
    if i == len_s:
        return True
    return False

print(isSubsequence("b", "abc"))
