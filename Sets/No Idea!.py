n, m = input().split()
n = int(n)
m = int(m)
arr = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
happiness = 0
for value in arr:
    if value in A:
        happiness +=1
    if value in B:
        happiness -=1
print(happiness)
    