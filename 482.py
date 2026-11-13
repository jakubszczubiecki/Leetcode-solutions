s = "5F3Z-2e-9-wa"
def licenseKeyFormatting(s, k):
    new_key = ""
    s = s.replace("-", "").upper()
    if len(s) % k == 0:
        for i in range(0, len(s), k):
            new_key += s[i:i+k]
            if i + k != len(s):
                new_key += "-"
    else:
        rest = len(s) % k
        new_key += s[0:rest]
        if k < len(s):
            new_key += "-"
        for i in range(rest, len(s), k):
            new_key += s[i:i+k]
            if i + k != len(s): 
                new_key += "-"
    return new_key
print(licenseKeyFormatting(s, 4))