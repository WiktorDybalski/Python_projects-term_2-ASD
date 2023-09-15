from zad3testy import runtests


class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return i * 2 + 1

    @staticmethod
    def right(i):
        return i * 2 + 2

    def insert(self, val):
        self.arr.append(val)
        self.size += 1
        i = self.size - 1
        while i > 0 and self.arr[i][0] < self.arr[self.parent(i)][0]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)

    def fix(self, i):
        l = self.left(i)
        r = self.right(i)
        m = i
        if l < self.size and self.arr[l][0] < self.arr[m][0]:
            m = l
        if r < self.size and self.arr[r][0] < self.arr[m][0]:
            m = r
        if m != i:
            self.arr[i], self.arr[m] = self.arr[m], self.arr[i]
            self.fix(m)

    def pop(self):
        if self.empty():
            raise IndexError("Pusto jak w mojej głowie na piuerwszych dwóch kolokwiach :((")
        root = self.arr[0]
        self.arr[0], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[0]
        self.arr.pop()
        self.size -= 1
        self.fix(0)
        return root

    def empty(self):
        return self.size == 0


def kintersect(A, k):
    n = len(A)
    B = [(A[i][0], A[i][1], i) for i in range(n)]
    B.sort(key=lambda x: x[0])
    res = 0
    H = Heap()
    temp = [None for _ in range(k)]
    for i in range(k - 1):
        H.insert((B[i][1], B[i][2]))
    for i in range(k - 1, n):
        H.insert((B[i][1], B[i][2]))
        begin = B[i][0]
        end, ind = H.pop()
        if res < end - begin:
            res = end - begin
            for j in range(k - 1):
                temp[j] = H.arr[j][1]
            temp[k - 1] = ind
    return temp


runtests(kintersect)
