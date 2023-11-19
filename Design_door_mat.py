N, M = map(int,input().split())

s = "WELCOME"
c = ".|."
cnt = 1
for i in range(N):
        if i == (N//2):
            print(s.center(M,'-'))
            cnt-=2
        else:
            print((c*cnt).center(M,'-'))
            if i < (N//2):
                cnt+=2
            else:
                cnt-=2