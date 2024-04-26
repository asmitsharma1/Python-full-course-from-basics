def bs(lst,n):
    l = 0
    r = len(lst)-1
    while l <= r:
        mid = (l+r)//2
        if lst[mid] == n:
            return mid
        elif lst[mid] < n:
            l = mid+1
        else:
            r = mid-1
    return -1
lst=[1,2,3,4,5,6,7,8,9,10]
n=5
result=bs(lst,n)
if result != -1:
    print("Element is present at index",str(result))
else:
    print("Element is not present in the list")