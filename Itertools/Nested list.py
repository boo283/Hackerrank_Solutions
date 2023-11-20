if __name__ == '__main__':
    arr = []
    arr_score = []
    arr_name = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
    for val in arr:
        arr_score.append(val[1])
        arr_name.append(val[0])
    
    min_score = (min(arr_score))
    arr_id = []
    for i in range(0,len(arr_score)):
        if min_score == arr_score[i]:
            arr_id.append(i)
    arr_id = sorted(arr_id, reverse= True)
    for val in arr_id:      
        arr_score.remove(arr_score[val])
        arr_name.remove(arr_name[val])
        arr.remove(arr[val])
    
    rs = []
    min_score = min(arr_score)
    for value in arr:
        if value[1] == min_score:
            rs.append(value[0])
    rs = sorted(rs)
    
    for val in rs:
        print(val)
