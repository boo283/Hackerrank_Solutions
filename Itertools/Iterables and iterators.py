import itertools
n = int(input())
s = input().split()
num_slice = int(input())

#s = s.replace(" ",'')

rs = list(itertools.combinations(s,num_slice))
cnt = 0
for c in rs:
    if 'a' in c:
        cnt+=1
print(f"{cnt/len(rs):.4f}")
