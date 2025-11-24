def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


quick_sorted = quicksort([5, 3, 1, 4, 2])
print(quick_sorted)  # вывод: [1, 2, 3, 4, 5]





