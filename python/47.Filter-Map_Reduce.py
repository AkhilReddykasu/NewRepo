"""47.Filter-Map_Reduce"""
from functools import reduce

# filter
li = [7, 8, 9, 4, 5, 6, 1, 2, 3]
even_num = list(filter(lambda n: n % 2 == 0, li))
print("Even num in list:", even_num)

# map

double = list(map(lambda a: a * a, even_num))
print("Doubling the even list:", double)

# reduce

add_all = reduce(lambda a, b: a + b, double)
print("Sum of all ele in double:", add_all)