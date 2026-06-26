#creating a node
#Singly Linked List
'''class node:
    def __init__(self,data):
        self.data = data
        self.next = None
n = node(10)
print("Data",n.data)
print("Next",n.next)'''

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

temp = head

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next'''

#insertion at end
'''class node:
    def __init__(self,data):
        self.data = data
        self.next = None
n = int(input("Enter no. of nodes: "))
head = None
tail = None
for i in range(n):
    data = int(input("Enter value:"))
    newnode = node(data)
    if head is None:
        head = newnode
        tail = newnode
    else:
        tail.next = newnode
        tail = newnode
print("Single Linked List")
temp = head
while temp:
    print(temp.data,end="->")
    temp = temp.next
print("None")'''

#insertion at head
'''class node:
    def __init__(self,data):
        self.data = data
        self.next = None
n = int(input("Enter no. of nodes: "))
head = None
tail = None
for i in range(n):
    data = int(input("Enter value:"))
    newnode = node(data)
    newnode.next=head
    head=newnode
print("Single Linked List")
temp = head
while temp:
    print(temp.data,end="->")
    temp = temp.next
print("None")
if head is None:
    print('stack empty........')
else:
    deleted=head.data
    head=head.next
    print('deleted element',deleted)
    
while temp:
    print(temp.data,end="->")
    temp = temp.next
print("None")'''

#insertion from start and delete from end
'''if head is None:
    print("Linked list is empty")
elif head.next is None:
    deleted_node=head.data
    head=None
    print("Deleted node:", deleted_node)
else:
    temp=head
    while temp.next.next:
        temp=temp.next
    deleted_node=temp.next.data
    temp.next=None
    print("Deleted node:", deleted_node)
print("Single Linked List after deleting ")
temp=head
while temp:
    print(temp.data, end="->")
    temp=temp.next
print("None")'''
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_end(head, data):
    """
    Insert a new node at the end of the linked list.
    """
    new_node = Node(data)

    if head is None:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next

    temp.next = new_node
    return head


def delete_at_end(head):
    """
    Delete the last node of the linked list.
    """
    if head is None:
        print("Linked list is empty")
        return None

    if head.next is None:
        print("Deleted node:", head.data)
        return None

    temp = head

    while temp.next.next:
        temp = temp.next

    print("Deleted node:", temp.next.data)
    temp.next = None

    return head


def display(head):
    """
    Display the linked list.
    """
    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")


# Create Linked List
n = int(input("Enter the number of nodes: "))

head = None

for i in range(n):
    data = int(input(f"Enter data for node {i + 1}: "))
    head = insert_at_end(head, data)

print("\nOriginal Linked List:")
display(head)

# Insert at End
value = int(input("\nEnter value to insert at end: "))
head = insert_at_end(head, value)

print("Linked List after insertion at end:")
display(head)

# Delete at End
head = delete_at_end(head)

print("Linked List after deletion at end:")
display(head)'''

#positional insertion in single linked list

'''class node:
    def __init__(self, data):
        self.data=data
        self.next=None
n=int(input("Enter the number of nodes: "))
head=None
for _ in range(n):
    data=int(input("Enter the data for node {}: ".format(_+1)))
    new_node=node(data)
    if head is None:
        head=new_node
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=new_node
data=int(input("Enter the data to insert at end: "))
pos=int(input("Enter the position to insert: "))
new_node=node(data)
if pos==0:
    new_node.next=head
    head=new_node
else:
    current=head
    for _ in range(pos-1):
        current=current.next
    new_node.next=current.next
    current.next=new_node
current=head
while current:
    print(current.data, end="->")
    current=current.next
print("None")'''

#Deletion at position
'''class node:
    def __init__(self,data):
        self.data = data
        self.next = None
n = int(input("Enter no. of nodes:"))
head = None
for _ in range(n):
    data = int(input("Enter value: "))
    if head is None:
        head = node(data)
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = node(data)
pos = int(input("Enter the position: "))
if head is None:
    pass
elif pos == 0:
    head = head.next
else:
    current = head
    for _ in range(pos-1):
        if current.next is None:
            break
        current = current.next.next
    if current.next:
        current.next = current.next.next
current = head
while current:
    print(current.data, end="->")
    current=current.next
print("None")'''

#doubly linked list insertion at end
'''class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
n=int(input("Enter the number of nodes: "))
head=None
tail=None
for i in range(n):
    data=int(input("Enter the data for node {}: ".format(i+1)))
    new_node=Node(data)
    if head is None:
        head=new_node
        tail=new_node
    else:
        tail.next=new_node
        new_node.prev=tail
        tail=new_node
if not head:
    print("The list is empty.")
else:
    print("Doubly linked list:")
    temp=head
    while temp:
        print(temp.data, end=" <-> ")
        temp=temp.next
    print("None")'''

#doubly linked list deletion at end
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


n = int(input("Enter the size of DLL: "))

head = None
tail = None

for i in range(n):
    value = int(input("Enter value: "))
    newnode = Node(value)

    if head is None:
        head = tail = newnode
    else:
        tail.next = newnode
        newnode.prev = tail
        tail = newnode


print("DLL:")
if head is None:
    print("DLL Empty..")
else:
    curr = head
    while curr:
        print(curr.data, end=" <-> ")
        curr = curr.next
    print("None")


# Delete last node
if head:
    if head == tail:
        head = tail = None
    else:
        tail = tail.prev
        tail.next = None


print("After deletion:")
if head is None:
    print("DLL Empty..")
else:
    curr = head
    while curr:
        print(curr.data, end=" <-> ")
        curr = curr.next
    print("None")
    while curr:
        print(curr.data,end="<->")
        curr=curr.next
    print("None")'''
