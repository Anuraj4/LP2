
def selectionSort(arr):
    for i in range(len(arr)):
        # In the provided code snippet, the line `min = float('-inf')` is actually not being used in
        # the selection sort algorithm. It seems to be a leftover line that is not necessary for the
        # sorting logic.
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
print(selectionSort(arr))
