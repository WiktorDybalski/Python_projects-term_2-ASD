# Bucket_sort for an array
# Sort only when the elements are from uniform distribution(rozkład jednostajny)
# Complexity: O(n + k), where n - amount of elements, k - max element
# Apr. Complexity: O(n)

array = [4, 2, 1, 6, 3, 7, 8, 9, 5, 11]
T = [2, 4, 6, 2, 2, 5, 7, 8, 3, 2, 76, 62, 25, 4, 45, 4, 34, 2, 5, 5757573, 23, 15346, 3453, 5, 52535]
# array called T is not form uniform distribution so sort is not correct for them


def Bucket_sort(array):
    n = len(array)
    buckets = [[] for _ in range(200)]

    for el in array:
        buckets_index = el % (200)
        buckets[buckets_index - 1] = el

    sorted_array = []
    for i in range(200):
        if not buckets[i]:
            continue
        sorted_array += [buckets[i]]
    return sorted_array


print(array)
print(Bucket_sort(array))
