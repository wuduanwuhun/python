#
# class Sort:
#     def __init__(self, n):
#         self.arr = [0] * n
#         self.len = n
#         self.random_data()
#
#         #n是排序的个数
#
#     def random_data(self):
#         for i in range(self.len):
#             self.arr[i] = random.randint(1, 100)
#
#     def partition(self, left, right):
#         arr = self.arr
#         k = i = left
#         for i in range(left, right):
#             if arr[i] < arr[right]:
#                 arr[i], arr[k] = arr[k], arr[i]
#                 k += 1
#         arr[right], arr[k] = arr[k], arr[right]
#         return k
#
#     def quick_sort(self, left, right):
#         if left < right:
#             pivot = self.partition(left, right)
#             self.quick_sort(left, pivot - 1)
#             self.quick_sort(pivot + 1, right)
#
#
# if __name__ == '__main__':
#     my_sort = Sort(10)
#     print(my_sort.arr)
#     my_sort.quick_sort(0, my_sort.len - 1)
#     print(my_sort.arr)

# 1.完成二叉树的建树，前序，中序，后序，层序遍历
# 二叉树建树
# from collections import deque
#
#
# class BiTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.lchild = None
#         self.rchild = None
#
#
# class CreateBiTree:
#     def __init__(self, str_tree):
#         self.str_tree = str_tree
#
#     def create_tree(self):
#         l1 = list(self.str_tree)
#         l1 = [None if i == '#' else i for i in l1]
#         nodes = [BiTreeNode(l1[i]) for i in range(len(l1))]
#         root = nodes[0]
#         for i in range(len(l1)):
#             if 2 * i + 2 > len(l1):
#                 break
#             cur_node = nodes[i]
#             if nodes[2 * i + 1].data:
#                 cur_node.lchild = nodes[2 * i + 1]
#             if nodes[2 * i + 2].data:
#                 cur_node.rchild = nodes[2 * i + 2]
#         return root
#
#     def __call__(self):
#         return self.create_tree()
#
#
# class BiTreeSorted:
#     def __init__(self, root):
#         self.root = root
#
#     def pre_order(self, root):
#         # 前序排列
#         if root:
#             print(root.data, end=',')
#             self.pre_order(root.lchild)
#             self.pre_order(root.rchild)
#
#     def in_order(self, root):
#         # 中序排列
#         if root:
#             self.in_order(root.lchild)
#             print(root.data, end=',')
#             self.in_order(root.rchild)
#
#     def post_order(self, root):
#         # 后序排列
#         if root:
#             self.post_order(root.lchild)
#             self.post_order(root.rchild)
#             print(root.data, end=',')
#
#     def level_order(self, root):
#         # 层序排列
#         queue = deque()
#         queue.append(root)
#         while len(queue) > 0:
#             node = queue.popleft()
#             print(node.data, end=',')
#             if node.lchild:
#                 queue.append(node.lchild)
#             if node.rchild:
#                 queue.append(node.rchild)
#
#     def __call__(self):
#         print('前序排列')
#         self.pre_order(self.root)
#         print()
#
#         print('中序排列')
#         self.in_order(self.root)
#         print()
#
#         print('后序遍历')
#         self.post_order(self.root)
#         print()
#
#         print('层序遍历')
#         self.level_order(self.root)
#         print()
#
#
# if __name__ == '__main__':
#     a = CreateBiTree('1234#560##789')
#     root = a()
#     print('根结点为：', root.data)
#     sorted = BiTreeSorted(root)
#     sorted()

# 2.完成sorted的练习
# 按字符串字母顺序排序
# fruits = ["date", "banana", "apple", "orange", "grape", "pear", "cherry", "yes"]
# result0 = sorted(fruits)
# print(result0)
#
# # 按字符串长度排序
# result1 = sorted(fruits, key=lambda x: len(x))
# print(result1)
#
# # 降序排序
# num = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# result2 = sorted(num, reverse=True)
# print(result2)
#
#
# class Person:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def __repr__(self):
#         return repr((self.name, self.age, self.weight))
#
#
# people = Person("Alice", 25, 40)
# People_objects = [
#     Person("Alice", 17, 40),
#     Person("Bob", 20, 60),
#     Person("Charlie", 21, 70),
#     Person("David", 35, 65),
#     Person("Eve", 16, 43),
# ]
#
# print(sorted(People_objects, key=lambda people: people.weight))
#
# from operator import itemgetter, attrgetter
# People_tuples = [("Alice", 17, 40),
#                  ("Bob", 20, 60),
#                  ("Charlie", 21, 70),
#                  ("David", 35, 65),
#                  ("Eve", 16, 43)]
# print(sorted(People_tuples, key=itemgetter(0)))
# print(sorted(People_objects,key=attrgetter('age')))
#
# print(sorted(People_tuples, key=itemgetter(1,2)))
# print(sorted(People_tuples, key=lambda x: (x[1],-x[2])))
# print(sorted(People_objects, key=attrgetter('weight', 'age'),reverse=True))
#
# data = [('apple',2),('banana',2),('apple',3),('banana',3)]
# print(sorted(data, key=itemgetter(0)))
#
# grademeau=[
#     {'name':'Alice','age':17,'score':80,'height':160}
#     ,{'name':'Bob','age':20,'score':70,'height':170}
#     ,{'name':'Charlie','age':21,'score':85,'height':165}
#     ,{'name':'David','age':35,'score':90,'height':180}
#     ,{'name':'Eve','age':16,'score':75,'height':155}
# ]
# print(sorted(grademeau,key=lambda x: (x['age'],-x['score'])))
# print(sorted(grademeau,key=itemgetter('age','score')))

# 3.完成快速排序，堆排序

# 快速排序
# import random
# class Sort:
#     def __init__(self, n):
#         self.arr = [0] * n
#         self.len = n
#         self.random_data()
#
#         #n是排序的个数
#
#     def random_data(self):
#         for i in range(self.len):
#             self.arr[i] = random.randint(1, 100)
#
#     def partition(self, left, right):
#         arr = self.arr
#         k = i = left
#         for i in range(left, right):
#             if arr[i] < arr[right]:
#                 arr[i], arr[k] = arr[k], arr[i]
#                 k += 1
#         arr[right], arr[k] = arr[k], arr[right]
#         return k
#
#     def quick_sort(self, left, right):
#         if left < right:
#             pivot = self.partition(left, right)
#             self.quick_sort(left, pivot - 1)
#             self.quick_sort(pivot + 1, right)
#
#
# if __name__ == '__main__':
#     my_sort = Sort(10)
#     print("初始序列：")
#     print(my_sort.arr)
#     my_sort.quick_sort(0, my_sort.len - 1)
#     print("排序后序列：")
#     print(my_sort.arr)

# 2.堆排序
import random
import heapq

tree = [random.randint(1, 101) for i in range(10)]
print(tree)
heapq.heapify(tree)
for i in range(len(tree)):
    tmp = heapq.heappop(tree)
    print(tmp,end=' ')