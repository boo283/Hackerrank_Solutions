import itertools
s = input()

arr_n = [list(n) for c, n in itertools.groupby(s)]
for num in arr_n:
    print("(%s, %s)" %(len(num),num[0]),end=' ')