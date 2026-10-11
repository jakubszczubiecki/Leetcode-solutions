def canConstruct(ransomNote, magazine):
    slownik_magazine = {}
    for i in magazine:
        if i in slownik_magazine:
            slownik_magazine[i] += 1
        else:
            slownik_magazine[i] = 1
    for i in ransomNote:
        if i in slownik_magazine:
            slownik_magazine[i] -= 1
        else:
            return False
    for i in slownik_magazine.values():
        if i < 0:
            return False
    return True
print(canConstruct("aac", "aabbbb"))