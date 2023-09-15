def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        arr = [num for bucket in buckets for num in bucket]
        exp *= 10
    return arr


# O(nm), where n is the number of elements and m is the length of the longest element
def radix_sort2(tab, x):
    if x == -1:
        return tab
    it = x
    output_0 = []
    output_1 = []
    for i in tab:
        if len(i) <= it:
            output_0 = [i] + output_0
        elif i[it] == '0':
            output_0.append(i)
        else:
            output_1.append(i)
    return radix_sort2(output_0 + output_1, x - 1)


arr = [2, 1, 4, 3, 1, 5, 2, 7, 8, 3]
radix_sort(arr)