n = int(input())
s = set(map(int,input().split()))
c = int(input())
for _ in range(c):
    t = input().split()
    if t[0] == 'pop':
        s.pop()
    elif t[0] == 'remove':
        if int(t[1]) in s:
            s.remove(int(t[1]))
    elif t[0] == 'discard':
        s.discard(int(t[1]))
print(sum(s))