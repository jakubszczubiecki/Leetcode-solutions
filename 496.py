nums1 = [4,1,2]
nums2 = [1,3,4,2]
def nextGreaterElement(nums1, nums2):
    ans = []
    znalezione = 0
    for i in range(len(nums1)):
        znalezione = 0
        for j in range(nums2.index(nums1[i])+1, len(nums2)):
            if nums1[i] < nums2[j]:
                ans.append(nums2[j])
                znalezione = 1
                break
        if znalezione != 1:
            ans.append(-1)
    return ans
print(nextGreaterElement(nums1,nums2))