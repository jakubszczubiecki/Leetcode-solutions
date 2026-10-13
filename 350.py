def intersect(nums1, nums2):
    slownik1 = {}
    slownik2 = {}
    tab_to_return = []
    for i in range(len(nums1)):
        if nums1[i] not in slownik1:
            slownik1[nums1[i]] = nums1.count(nums1[i])
    for i in range(len(nums2)):
            if nums2[i] not in slownik2:
                slownik2[nums2[i]] = nums2.count(nums2[i])
    for klucz in slownik2.keys():
        if klucz in slownik1:
            if slownik1[klucz] > slownik2[klucz]:
                tab_to_return += [klucz] * slownik2[klucz]
            elif slownik1[klucz] < slownik2[klucz]:
                tab_to_return += [klucz] * slownik1[klucz]
            else:
                tab_to_return += [klucz] * slownik2[klucz]
    return tab_to_return

tab1 = [1,2,2,1]
tab2 = [2,2]
print(intersect(tab1, tab2))