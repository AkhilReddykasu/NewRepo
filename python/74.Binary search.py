# Binary search

pos = -1


def search(lst, i):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == i:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < i:
                low = mid + 1
            else:
                high = mid - 1
    return False


li = [5, 6, 7, 8, 9, 12, 13, 58, 96, 99, 105, 203, 708, 809, 810]
n = int(input('Enter a number you want to search for :'))
if search(li, n):
    print('searched element in list: ', pos)
else:
    print('not found in list')
