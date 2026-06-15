#Queue Data structures - FIFO
'''
Tail - insertion
Head - deletion
               ----------
Head(insertion)|10|20|30| Tail(Deletion)
               ----------
Overflow: Condition when insertion is attempted in a full data structure.
Underflow: Condition when deletion is attempted from an empty data structure.
isEmpty(): A method or check used to determine whether the data structure
has no elements.
enqueue - append
dequeue - pop(i)
peak[0]

Import queue
1. Add item -> append(x) -> put(x)
2. Remove item -> popleft(x)/pop(i) -> get(x)
3. size -> q.qsize()
4. empty -> q.empty()'''


'''from queue import Queue
q=Queue()
q.put(1)
q.put(2)
print(list(q.queue))
print("front element:", q.queue[0])
print("rear element:", q.queue[-1])
print("Size of queue:", q.qsize())
print(q.get())
print(q.get())
print(list(q.queue))
if q.empty():
    print("Queue is empty")
else:
    print("Queue has:", list(q.queue))
print("Size of queue:", q.qsize())'''


#implementation of stack using queue
'''from queue import Queue as queue
class stack:
    def __init__(self):
        self.q1=queue()
        self.q2=queue()
    def push(self, x):
        self.q1.put(x)
    def pop(self):
        if self.q1.empty():
            return None
        while self.q1.qsize()>1:
            self.q2.put(self.q1.get())
        res=self.q1.get()
        self.q1,self.q2=self.q2,self.q1
        return res
    def top(self):
        if self.q1.empty():
            return None
        while self.q1.qsize()>1:
            self.q2.put(self.q1.get())
        res=self.q1.get()
        self.q2.put(res)
        self.q1,self.q2=self.q2,self.q1
        return res
    def empty(self):
        return self.q1.empty()
s=stack()
s.push(1)
s.push(2)
print(s.top())
print(s.pop())
print(s.top())
print(s.empty())'''


'''from queue import Queue
class stack:
    def __init__(self):
        self.q=Queue()
    def push(self,x):
        size=self.q.qsize()
        self.q.put(x)
        for i in range(size):
            self.q.put(self.q.get())
    def pop(self):
        if self.q.empty():
            print('stack empty.....')
        else:
            print('popped',self.q.get())
    def top(self):
        if self.q.empty():
            print("Stack empty")
        else:
            print("Top:",self.q.queue[0])
    def display(self):
        print("Stack:",list(self.q.queue))
s = stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.top()
s.pop()
s.display()'''

#Stack using 2 queues
'''from queue import Queue
q1 = Queue()
q2 = Queue()
q1.put(10)
q1.put(11)
q1.put(12)
while q1.qsize()>1:
    q2.put(q1.get())
print("Popped",q1.get())
while not q2.empty():
    q1.put(q2.get())
print("Remaining stack:",list(q1.queue))'''

#Dequeue (Double Ended Queue)
'''from collections import deque
d = deque()
d.append(10)       # Rear
d.append(20)
d.appendleft(5)    # Front
print(d)
d.pop()            # Remove from rear
print(d)
d.popleft()        # Remove from front
print(d)
'''


#Deque - Double ended queue
'''Left Deletion
Right Insertion
Insertion and deletion can be performed on both sides

import deque -> collections
operations:
    append()  1 2 3 <- 4  1 2 3 4
    appendleft()  4-> 1 2 3   4 1 2 3
    pop()  1 2 3 4->4  1 2 3
    popleft()  1 2 3 4   2 3 4

#Insertion at front and rear
from collections import deque
d = deque()
d.append(10)
d.append(20)
d.append(30)
print(d)
d.appendleft(1)
d.appendleft(2)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
print(d.count(1))
d.reverse()
print(d)
d.rotate()
print(d)
d.rotate(-1)
print(d)
d.extend([22,33,44])
print(d)
d.extendleft([111,222,333])
print(d)
d.clear()
print(d)'''

#deque
'''from collections import deque
arr=[1,2,3,4,5]
d=deque(arr)
d.append(10)
d.append(20)
d.appendleft(30)
d.appendleft(60)
print("display")
for data in d:
    print(data,end=' ')
d.rotate(-2)
print("after rotating")
print()
for data in d:
    print(data,end=' ')
print()
print("popping element",d.pop())
print("popping element left",d.popleft())
print("after popping")
for data in d:
    print(data,end=' ')

#maxlength
print()
print("maxlen in a deque")
dque2=deque(maxlen=3)
dque2.append(2)
dque2.append(3)
dque2.append(4)
dque2.append(5)
#what we expect 2 3 4 5 but we get 3 4 5 as a result because it follows fifo whn we specify maxlen and drops the first element
for dd in dque2:
    print(dd,end=' ')'''

#Write a program to check if a string is palindrome or not using deque
'''from collections import deque
s = input("String: ").lower()
d = deque(s)
palindrome = True

while len(d) > 1:
    if d.popleft() != d.pop():
        palindrome = False
        break

if palindrome:
    print(s,"is a Palindrome")
else:
    print(s,"is not a Palindrome")'''

'''from collections import deque
n=input()
print(n)
a=deque(n)
a.rotate(len(a))
if a==n:
    print('it is a palindrome')
else:
    print('it is not a palindrome')'''

#Reverse a string using deque
'''from collections import deque
s = input("Enter string:")
d = deque(s)
rev=''
while d:
    rev+=d.pop()
int(rev)'''


#heap queue
'''heapq
import heapq
from collections
heappush()
heappoop()
heappushpop()
heapreplace()
nlargest()
nsmallest()
merge()
clear()
heapify()'''

'''import heapq
h = []
heapq.heappush(h, 30)
heapq.heappush(h, 10)
heapq.heappush(h, 20)
heapq.heappush(h, 40)
print(h)
print(heapq.heappop(h))
print(h)
print(heapq.heappushpop(h,7))
print(heapq.heapreplace(h,7))
print(h)
print(heapq.nlargest(2,h))
print(heapq.nsmallest(2,h))
a=[1,2,3]
b=[4,5,6]
print(list(heapq.merge(a,b)))
h.clear()
print(h)
#Using nlargest() (Easiest)
arr = [10, 40, 20, 50, 30]
print(heapq.nlargest(2, arr)[1])'''
#priority heapq
'''import heapq
pq=[]
heapq.heappush(pq,(1,"emergency"))
heapq.heappush(pq,(3,"follow up"))
heapq.heappush(pq,(2,"consultation"))
while pq:
    print(heapq.heappop(pq))'''

#min priority heapq
'''import heapq
pq=[]
n=int(input('enter size:'))
for i in range(n):
    val=int(input('enter value:'))
    heapq.heappush(pq,val)
print('\n min priority queue')
print('\n elements removed in min priority order:')
while pq:
    print(heapq.heappop(pq),end=' ')'''


'''import heapq
pq=[]
n=int(input('enter size:'))
for i in range(n):
    val=int(input('enter value:'))
    heapq.heappush(pq,-val)
print('\n max priority queue')
print('\n elements removed in max priority order:')
while pq:
    print(-heapq.heappop(pq),end=' ')'''

'''arr = list(map(int,input().split()))
n = len(arr)
for i in range(n):
    for l in range(n-i-1):
        if arr[l]>arr[l+1]:
            arr[l],arr[l+1]=arr[l+1],arr[l]
k=int(input('which largest element'))
print(arr[-k])'''
