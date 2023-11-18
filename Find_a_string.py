def count_substring(string, sub_string):
    cnt = 0
    str = string
    while sub_string in str:
        idx = str.find(sub_string)
        cnt+=1
        str = str[:idx] + ' ' + str[idx+1:]
    return cnt

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)