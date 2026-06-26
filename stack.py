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
'''nums=list(map(int,input("Enter the numbers: ").split()))
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
print("Odd numbers:",y)'''

#----------------------------
'''stack=[]
n=int(input('enter the size of the stack'))
for i in range(n):
    v=int(input('enter the value'))
    stack.append(v)
stack.append(11)
stack.append(22)
stack.append(33)
print(*stack)
print('removed',stack.pop())
print('peak',stack[-1])
print('size',len(stack))'''
#stack is empty or full
'''max=int(input('enter stack size'))
stack=[]
n=int(input('enter the elements'))
for i in range(n):
    if len(stack)<max:
        stack.append(int(input()))
    else:
        print('stack overflow')
        break
print('stack:',stack)
if len(stack)==0:
    print('stack is empty')
else:
    print('stack is not empty ')
if len(stack)==max:
    print('stack is full')
else:
    print('stack is not full')'''

#undo redo operations using stack
'''undostack=[]
redostack=[]
file='data.txt'
while True:
    print('\n 1.Write')
    print('2.undo')
    print('3.redo')
    print('4.view')
    print('5.exit')
    choice=int(input('enter choice'))
    if choice==1:
        text=input('enter text')
        undostack.append(text)
        redostack.clear()
        with open(file,'w') as f:
            f.write(text)
    elif choice==2:
        if (len(undostack)>1):
            redostack.append(undostack.pop())
            with open(file,'w') as f:
                f.write(undostack[-1])
            print("undo completed..")
        else:
            print("nothing to undo")
    elif choice==3:
        if redostack:
            text=redostack.pop()
            undostack.append(text)
            with open(file,'w') as f:
                f.write(text)
            print("redo completed")
        else:
            print("nothing to redo")
    elif choice==4:
        with open(file,'r') as f:
            print("file content",f.read())
    elif choice==5:
        break'''

#Expressions using stack
#Infix to prefix expression
'''def precedence(op):
    if op in ('+','-'):
        return 1
    if op in ('*','/'):
        return 2
    if op in ('^'):
        return 3
    return 0
def infixtoprefix(expr):
    expr = expr[::-1]
    temp=''
    for ch in expr:
        if ch=='(':
            temp+=')'
        elif ch==')':
            temp+='('
        else:
            temp+=ch
    stack = []
    postfix = ''
    for ch in temp:
        if ch.isalnum():
            postfix+=ch
        elif ch=='(':
            stack.append(ch)
        elif ch==')':
            while stack and stack[-1]!='(':
                postfix+=stack.pop()
            stack.pop()
        else:
            while (stack and precedence(stack[-1])>=precedence(ch)):
                postfix+=stack.pop()
            stack.append(ch)
    while stack:
        postfix+=stack.pop()
    prefix = postfix[::-1]
    return prefix
expr = input("Enter an infix expression: ")
print("Prefix expression:",infixtoprefix(expr))'''

#Evaluation of prefix expression *+234->20

'''stack = []
expr = input("Enter expression: ")
for i in reversed(expr):
    if i.isdigit():
        stack.append(int(i))
    else:
        one = stack.pop()
        two = stack.pop()
        if i=='+':
            stack.append(one+two)
        elif i=='-':
            stack.append(one-two)
        elif i=='*':
            stack.append(one*two)
        elif i=='/':
            stack.append(one//two)
print(stack.pop())'''

#conversion of infix to postfix

'''def prec(op):
    if op in '+-':
        return 1
    if op in '*/':
        return 2
    return 0
infix=input("Enter Expression:")
stack=[]
postfix=''
for ch in expr:
    if ch.isalnum():
        postfix+=ch
    else:
        while stack and prec(stack[-1]>= prec(ch)):
            postfix+=stack.pop()
        stack.append(ch)
while stack:
    postfix+= stack.pop()
print(postfix)'''


'''implementation of stack:
motonic stack
1.increasing
2.decreasing
3.valid parenthesis
i.check balanced
ii.balance the unbalanced
iii.delete the balanced
bottom-> 3 1 4 2 6 8->top
[]->push 3
[3]->push 1? is 3 smaller than 1 false ->pop()
[]
[1]->push 1
[1]->push 4> is greater than 1 true ->push 4
[1,4]->push 2? is greater than 4 pop 4
[1]-> push 1
[1,2]->2->6
[1,2,6]
[1,2,6,8]
input data
3 1 4 2 6 8
1 2 6 8 '''


#increasing monotonic
'''stack=[]
nums=list(map(int,input().split()))
for x in nums:
    while stack and stack[-1]>x:
        stack.pop()
    stack.append(x)
print(stack)'''

#decreasing monotonic
'''stack=[]
nums=list(map(int,input().split()))
for x in nums:
    while stack and stack[-1]<x:
        stack.pop()
    stack.append(x)
print(stack)'''


'''nums = list(map(int, input().split()))

result = []

# index 0, 2, 4 ...
for i in range(0, len(nums), 2):
    result.append(nums[i])

# index 3, 1 ... reverse odd positions
for i in range(1,len(nums),2):
    result.append(nums[i])

print(*result)'''


#Balanced paranthesis or not
'''s = input("Enter expression: ")
stack = []
pairs = {')':'(',']':'[','}':'{'}
balanced = True
for ch in s:
    if ch in '([{':
        stack.append(ch)
    elif ch in ')]}':
        if not stack or stack[-1]!=pairs[ch]:
            balanced = False
            break
        stack.pop()
if stack:
    balanced = False
if balanced:
    print(s,"is balanced")
else:
    print(s,"is not balanced")'''


'''s = input("Enter expression: ")
stack = []
pairs = {')': '(', ']': '[', '}': '{'}
rev_pairs = {'(': ')', '[': ']', '{': '}'}
result = []

for ch in s:
    if ch in '([{':
        stack.append(ch)
        result.append(ch)
    elif ch in ')]}':
        if stack and stack[-1] == pairs[ch]:
            stack.pop()
            result.append(ch)
        else:
            result.append(pairs[ch])
            result.append(ch)
    else:
        result.append(ch)
while stack:
    open_bracket = stack.pop()
    result.append(rev_pairs[open_bracket])

print("Balanced:", "".join(result))'''
