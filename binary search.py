#binary search
'''arr=list(map(int,input('enter values').split()))
target=int(input('enter target:'))
left=0
right=len(arr)-1
found=False
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print('element found at index',mid)
        found=True
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
if not found:
    print('element not found..........')'''



#binary search lowerbound
'''arr=list(map(int,input('enter values').split()))
target=int(input('enter target:'))
left=0
right=len(arr)-1
ans=len(arr)
while left<=right:
    mid=(left+right)//2
    if arr[mid]>=target:
        ans=mid
        right=mid-1
    else:
        left=mid+1
print('lower bound',ans)'''
#binary search upperbound
'''arr=list(map(int,input('enter values').split()))
target=int(input('enter target:'))
left=0
right=len(arr)-1
ans=len(arr)
while left<=right:
    mid=(left+right)//2
    if arr[mid]>target:
        ans=mid
        right=mid-1
    else:
        left=mid+1
print('upper bound',ans)'''


#binary search first occurance
'''arr=list(map(int,input('enter values').split()))
target=int(input('enter target:'))
left=0
right=len(arr)-1
first=-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        first=mid
        right=mid-1
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid+1
print('first occurance',first)'''


#binary search last occurance
'''arr=list(map(int,input('enter values').split()))
target=int(input('enter target:'))
left=0
right=len(arr)-1
last=-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        last=mid
        left=mid+1
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
print('last occurance',last)'''
#square root

n = int(input('enter value'))
low = 0
high = n

while low <= high:
    mid = (low + high) // 2
    if mid * mid == n:
        print(mid)
        break
    elif mid * mid < n:
        low = mid + 1
    else:
        high = mid - 1
