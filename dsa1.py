'''n=int(input())
for i in range(n):
    for k in range(n):
        if i==0 or k==0 or (i+k)==n-1 or i==n-1 or k==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''n=int(input())
for i in range(n):
    for k in range(n):
        if i==0 or k==0 or (i+k)==n-1 or i==n-1 or k==n-1 or i==k:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#nivens number
'''n = int(input("Enter number: "))
c = n
sum_n = 0
while n!=0:
    r = n%10
    sum_n += r
    n //= 10
if c%sum_n==0:
    print("Niven's Number")
else:
    print("Not niven's number")'''


#strong number and Krishnamurthy number
'''import math
n=int(input())
a=n
c=0
while n>0:
    b=n%10
    c+=math.factorial(b)
    n=n//10
if a==c:
    print('it is a strong number')
else:
    print('it is not a strong number')'''

#    
