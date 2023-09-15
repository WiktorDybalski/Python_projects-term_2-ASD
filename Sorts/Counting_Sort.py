# Counting_Sort for an array
# Complexity: O(n + k), where n - amount of elements, k - max element
# Apr. Complexity: O(n)

array = [4, 2, 1, 6, 3, 7, 8, 9, 3, 10, 3, 5, 3, 6, 7]
array_mod = [[4, 2, 1], [6, 3, 7], [8, 9, 3], [10, 3, 5], [3, 6, 7]]


# Counting_Sort for an array

def Counting_Sort(array):
    n = len(array)
    k = max(array)
    amount_of_el = [0 for _ in range(k + 1)]
    sorted_array = [0 for z in range(n)]
    for i in range(n):
        amount_of_el[array[i]] += 1

    for j in range(1, k + 1):
        amount_of_el[j] += amount_of_el[j - 1]

    for s in range(n):
        sorted_array[amount_of_el[array[s]] - 1] = array[s]
        amount_of_el[array[s]] -= 1
    return sorted_array


# Counting_Sort for index i

def Counting_Sort_for_index(arr, index):
    n = len(arr)
    max_val = arr[0][index]
    for i in range(1, n):
        if arr[i][index] > max_val:
            max_val = arr[i][index]
    count = [0] * (max_val + 1)
    for i in range(n):
        count[arr[i][index]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    result = [None] * n
    for i in range(n - 1, -1, -1):
        result[count[arr[i][index]] - 1] = arr[i]
        count[arr[i][index]] -= 1
    return result


print(array_mod)
for i in range(2, -1, -1):
    print(Counting_Sort_for_index(array_mod, i))
