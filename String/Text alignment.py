# Enter your code here. Read input from STDIN. Print output to STDOUT

w = int(input()) 
c = 'H'

#Top Cone
for i in range(w):
    print((c*i).rjust(w-1)+c+(c*i).ljust(w-1))

#Top Pillars
for i in range(w+1):
    print((c*w).center(w*2)+(c*w).center(w*6))

#Middle Belt
for i in range((w+1)//2):
    print((c*w*5).center(w*6))    

#Bottom Pillars
for i in range(w+1):
    print((c*w).center(w*2)+(c*w).center(w*6))    

#Bottom Cone
for i in range(w):
    print(((c*(w-i-1)).rjust(w)+c+(c*(w-i-1)).ljust(w)).rjust(w*6))