# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    list3 = list1 + list2
    list3.sort()
    print(list3)


l1 = [100,4,53,6]
l2 = [4,54,65,999]
linear_merge(l1,l2)