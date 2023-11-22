from collections import Counter
n = int(input())
cm = list(map(int,input().split()))
stock = Counter(cm)
c = int(input())
price = 0
cmd = []
for i in range(c):
    cmd.append(list(map(int,input().split())))
for value in cmd:
    if stock[value[0]] > 0:
        price += value[1]
        stock[value[0]] -= 1
print(price)
