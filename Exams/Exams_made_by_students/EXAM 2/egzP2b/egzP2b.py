import bisect

from egzP2btesty import runtests
from math import log10


class BST_Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.x = 0


def add(root, string):
    if string == "":
        root.x += 1
        return
    root.x += 1
    if string[-1] == "1":
        if not root.left:
            root.left = BST_Node()
        add(root.left, string[:-1])
    else:
        if not root.right:
            root.right = BST_Node()
        add(root.right, string[:-1])
    return


def add_prefix(root, string):
    if string == "":
        return root.x
    if string[-1] == "1":
        return add_prefix(root.left, string[:-1])
    else:
        return add_prefix(root.right, string[:-1])


def kryptograf(D, Q):
    root = BST_Node()
    output = 1
    for i in D:
        add(root, i)
    for i in Q:
        output *= add_prefix(root, i)

    return log10(output)


# The best complexity: O(nm + qm)

# The complexity: O(nm + qmlogn)
# def radix_sort2(tab, x):
#     if x == -1:
#         return tab
#     it = x
#     output_0 = []
#     output_1 = []
#     for i in tab:
#         if len(i) <= it:
#             output_0 = [i] + output_0
#         elif i[it] == '0':
#             output_0.append(i)
#         else:
#             output_1.append(i)
#     return radix_sort2(output_0 + output_1, x - 1)
#
#
# def kryptograf(D, Q):
#     maxi = 0
#     for i in range(len(D)):
#         D[i] = D[i][::-1]
#         maxi = max(maxi, len(D[i]))
#     for i in range(len(Q)):
#         Q[i] = Q[i][::-1]
#     D = radix_sort2(D, maxi)
#     output = 1
#     for i in Q:
#         lo = bisect.bisect_left(D, i)
#         hi = bisect.bisect_right(D, i + "2")
#         output *= hi - lo
#     return log10(output)


# The base complexity: O(n^2logn + qmlogn)
# def kryptograf(D, Q):
#     for i in range(len(D)):
#         D[i] = D[i][::-1]
#     for i in range(len(Q)):
#         Q[i] = Q[i][::-1]
#     D = sorted(D)
#     output = 1
#     for i in Q:
#         lo = bisect.bisect_left(D, i)
#         hi = bisect.bisect_right(D, i + "2")
#         output *= hi - lo
#     return log10(output)


# The worst complexity: O(nmq)
# def kryptograf(D, Q):
#     cnt = 1
#     nd = len(D)
#     nq = len(Q)
#     temp_cnt = [0 for _ in range(nq)]
#     for i in range(nd):
#         temp = D[i]
#         j = 0
#         leng = len(temp)
#         while temp:
#             temp = D[i][j:leng:]
#             j += 1
#             for k in range(nq):
#                 if Q[k] == temp:
#                     temp_cnt[k] += 1
#     for i in range(nq):
#         cnt *= temp_cnt[i]
#
#     return log10(cnt)


# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests=0)
