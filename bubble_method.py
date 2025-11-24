def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


bubble_sorted = bubble_sort([5, 3, 1, 4, 2])
print(bubble_sorted)  # вывод: [1, 2, 3, 4, 5]
