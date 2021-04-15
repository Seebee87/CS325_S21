def helper_1(array, start, total):
    total = total + array[start +1]
    if start == len(array):
        return total