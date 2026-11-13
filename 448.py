nums = [4,3,2,7,8,2,3,1]
#1
def findDisappearedNumbers(nums):
    tab = set(nums)
    tab1 = []
    for i in range(1, len(nums)+1):
        if i not in tab:
            tab1.append(i)
    return tab1
print(findDisappearedNumbers(nums))
#2
#def findDisappearedNumbers1(nums):
