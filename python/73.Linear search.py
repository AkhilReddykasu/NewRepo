# Linear Search
pos = 0


def search(lst, j):
    for i in lst:
        if i == j:
            globals()['pos'] = lst.index(i)
            return True
    return False


li = [7, 82, 6, 41, 8, 89]
n = int(input('Enter a number you want to search for :'))
if search(li, n):
    print('searched element in list: ', pos)
else:
    print('not found in list')
