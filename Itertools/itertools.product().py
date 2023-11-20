import itertools as it
A = list(map(int,input().split()))
B = list(map(int,input().split()))

rs = sorted(list(it.product(A,B)))
print(*rs)
