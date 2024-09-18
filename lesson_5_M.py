# Урок №5. Стек и очередь

# Реализация стека через list() в Python:

# class Stack:а
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def push(self, item):
#         self.items.append(item)
   
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             print("Стек пуст. Мы не можем удалить из него элемент.")
    
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             print("Стек пуст. Мы не можем прочитать верхний элемент.")
    
#     def size(self):
#         return len(self.items)

# Протестируем код на входных данных: 

# stack = Stack()
# print(stack.is_empty()) 
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.size())     
# print(stack.peek())     
# item = stack.pop()
# print(item)             
# print(stack.size())    

# print('-------------------------------------------------------------')

# Реализация стека через связный список: 

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.head = None
   
#     def is_empty(self):
#         return self.head is None
    
#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
   
#     def pop(self):
#         if not self.is_empty():
#             popped = self.head
#             self.head = self.head.next
#             return popped.data
#         else:
#             print("Стек пуст. Мы не можем удалить из него элемент.")
       
#     def peek(self):
#         if not self.is_empty():
#             return self.head.data
#         else:
#             print("Стек пуст. Мы не можем прочитать верхний элемент.")

#     def size(self):
#         count = 0
#         current = self.head
#         while current:
#             count += 1
#             current = current.next
#         return count

# Протестируем код на входных данных:

# stack = Stack()
# print(stack.is_empty()) 
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.size())     
# print(stack.peek())     
# item = stack.pop()
# print(item)             
# print(stack.size())    

# print('-------------------------------------------------------------')

# Реализация очереди через list() в Python:

# class Queue:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def enqueue(self, item):
#         self.items.append(item)
   
#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         else:
#             print("Очередь пуст. Мы не можем удалить из него элемент.")
    
#     def peek(self):
#         if not self.is_empty():
#             return self.items[0]
#         else:
#             print("Очередь пуст. Мы не можем прочитать верхний элемент.")
    
#     def size(self):
#         return len(self.items)

# Протестируем код на входных данных:

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.dequeue()) 
# print(q.peek())    
# print(q.size())     
# print(q.is_empty()) 

# print('-------------------------------------------------------------')

# Реализация очереди через модуль queue:

# import queue
# q = queue.Queue()
# q.put(1)  
# q.put(2)
# q.put(3)
# print(q.get()) 
# print(q.get()) 
# print(q.qsize())
# print(q.empty())

# print('-------------------------------------------------------------')

# Реализация двусторонней очереди через модуль collection:

# from collections import deque
# d = deque([1, 2, 3])
# d.append(4)
# d.appendleft(0)
# last_element = d.pop()
# first_element = d.popleft()
# print(d)  
# print(last_element)  
# print(first_element) 

# print('-------------------------------------------------------------')

# Практическая задача:
# При написании кода необходимо использовать класс Stack, реализованный в начале занятия

# def is_balanced(s):
#     stack = Stack()
#     bracket_map = {')': '(', ']': '[', '}': '{'}
    
#     for char in s:
#         if char in bracket_map:
#             if stack:
#                 top_element = stack.pop()
#             else:
#                 '#'
#             if bracket_map[char] != top_element:
#                 return False
#         else:
#             stack.append(char)
    
#     return not stack

# Протестируем код на входных данных:

# s = "{[()()]}"
# result = is_balanced(s)
# print(result)  