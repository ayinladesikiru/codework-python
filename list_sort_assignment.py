from collections import Counter


def list_sorter(l):
    l_list = Counter(l)
    return [x for x, _ in sorted(l_list.items(), key=lambda x: x[1], reverse=True)]


l = [1, 1, 7, 7, 6, 9, 0, 7, 3, 0, 1, 4, 6, 0, 5]

print(list_sorter(l))

# without function
# n = 0
# while n < len(l):
#     n += 1
# print(n)
#
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]
# print(l)
#
# y = [num for num in l]
# print(y)
#
# b = ((1, 2), (3, 4))
# c = [sum(n) for n in b]
# print(c)
