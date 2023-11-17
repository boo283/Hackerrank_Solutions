def merge_the_tools(string, k):
    n = len(string)
    i = 0
    arr = []
    while(True):
        txt = string[i:i+k]
        arr.append(txt)
        i += k
        if i == n:
            break
    arr_1 = []
    for txt in arr:
        for i in range(len(txt)):
            if txt[i] not in arr_1:
                arr_1.append(txt[i])
        print(*arr_1, sep='')
        arr_1 = []
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)