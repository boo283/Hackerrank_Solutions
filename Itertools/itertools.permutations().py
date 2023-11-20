import itertools as it
s, n = input().split()
n = int(n)
arr_s = it.permutations(s,n)
arr_s = sorted(arr_s)
for s in arr_s:
    print(*s,sep ='')