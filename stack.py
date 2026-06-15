#STACKS
'''stack = []
item = int(input("Enter element to push: "))
stack.append(item) #push element to stack
print(stack)

stack = []
elements = list(map(int,input().split()))
for ele in elements:
    stack.append(ele)
print(stack)'''

'''stack = []
n = int(input("Size: "))
for i in range(n):
    v = int(input("Value: "))
    stack.append(v)
print(stack)
if len(stack)==0:
    print("Stack is empty!!")
else:
    print("Popped element: ",stack.pop())
print(stack)
print("Peek element: ",stack[-1])'''

'''stack=[]
size=int(input("stack size:"))
for i in range(size+1):

    item=int(input("enter num:"))
    if len(stack)==size:
        print("stack overflow...")
        break
    else:
        stack.append(item)
print("stack",*stack)'''

'''stack=[]
max_len=3
def push(item):
    if len(stack)==max_len:
        print("stack overflow")
    else:
        stack.append(item)
        print(item,"pushed")

for i in range(4):
    push(i)'''

#Applications of stack

#1. Reverse a string using stacks
#rev a string using stacks
'''s=input("enter a string: ")
stack=[]
for ch in s :
    stack.append(ch)
rev=''
while stack:
    rev+=stack.pop()
print("reversed string:",rev)'''

#Balanced paranthesis
'''s=input('enter braces')
stack=[]
balanced=True
for ch in s:
    if ch=='(':
        stack.append(ch)
    elif ch==')':
        if not stack :
            balanced=False
            break
        stack.pop()
if stack:
    balanced=False
if balanced:
    print('balanced')
else:
    print('not')'''

#balance the parenthesis if  not balanced by add
'''s=input("enter the braceses:")
stack=[]
balanced=0
for ch in s:
    if ch=='(':
        stack.append(ch)
    elif ch ==')':
        if stack:
            stack.pop()
        else:
            balanced+=1
balanced='('*balanced+s+')'*len(stack)
print(balanced)'''


#balance the parenthesis if  not balanced by sub
'''s=input("enter the braceses:")
stack=[]
remove=set()
for i in range(len(s)):
    if s[i]=='(':
        stack.append(i)
    elif s[i]==')':
        if stack:
            stack.pop()
        else:
            remove.add(i)
while stack:
    remove.add(stack.pop())
result=""
for i in range(len(s)):
    if i not in remove:
        result+=s[i]
print(result)'''

#find binary
'''n=int(input())
stack=[]
while n>0:
    stack.append(n%2)
    n//=2
print("Binary",end="")
while stack:
    print(stack.pop(),end=' ')'''

#increasing monotonic stack
'''n=int(input())
nums=list(map(int,input().split()))
stack=[]
for num in nums:
    while stack and stack[-1]>num:
        stack.pop()
    stack.append(num)
print(stack)'''

#bitonic 
nums=list(map(int,input("Enter the numbers: ").split()))
stack=[]
for num in nums:
    stack.append(num)
print("Stack is:",stack)    
x=[]
y=[]
while stack:
    num=stack.pop()
    if num%2==0:
        x.append(num)
    else:
        y.append(num)
print("Even numbers:",x)
print("Odd numbers:",y)
