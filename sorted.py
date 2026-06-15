#bubble sort
'''arr = list(map(int,input().split()))
n = len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr)'''

#selection sort

'''arr = list(map(int,input().split()))
n = len(arr)
for i in range(n-1):
    mini = i
    for j in range(i+1,n):
        if arr[j]<arr[mini]:
            mini = j
    arr[i],arr[mini]=arr[mini],arr[i]
print(*arr)'''

#insertion sort

'''arr = list(map(int,input().split()))
for i in range(1,len(arr)):
    key = arr[i]
    j = i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(*arr)'''

#merge sort
'''def merg(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merg(left)
        merg(right)
        i=k=l=0
        while i<len(left)and k<len(right):
            if left[i]<right[k]:
                arr[l]=left[i]
                i+=1
            else:
                arr[l]=right[k]
                k+=1
            l+=1
        while i<len(left):
            arr[l]=left[i]
            i+=1
            l+=1
        while k<len(right):
            arr[l]=right[k]
            k+=1
            l+=1
arr=list(map(int,input().split()))
merg(arr)'''

#counting sort
'''arr=list(map(int,input().split()))
ma=max(arr)
count=[0]*(ma+1)
for num in arr:
    count[num]+=1
s=[]
for i in range(len(count)):
    s.extend([i]*count[i])
print(s)'''

#quick sort
'''def qsort(arr):
    if len(arr)<=1:
        return arr
    p = arr[len(arr)//2]
    left = [x for x in arr if x<p]
    right = [x for x in arr if x>p]
    middle = [x for x in arr if x==p]
    return qsort(left)+middle+qsort(right)
arr = list(map(int,input("Enter elements: ").split()))
print(qsort(arr))'''

#flip sort

'''def flip(arr,k):
    arr[:k] = arr[:k][::-1]
def pancakesort(arr):
    n = len(arr)
    for size in range(n,1,-1):
        maxindex = arr.index(max(arr[:size]))
        if maxindex!=size-1:
            flip(arr,maxindex+1)
            flip(arr,size)
    return arr
arr = list(map(int,input("Enter elements: ").split()))
print(pancakesort(arr))'''
