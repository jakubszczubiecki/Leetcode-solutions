list = [1,1,1,1,1,1,2,3,4]
def distributeCandies(candyType):
    length = len(candyType)
    no_duplicates = set(candyType)
    if len(no_duplicates) < length // 2:
        return len(no_duplicates)
    else:
        return length // 2

#2
def distributecandies1(candyType):
    return min(len(set(candyType)), len(candyType) // 2)
print(distributeCandies(list))
print(distributecandies1(list))