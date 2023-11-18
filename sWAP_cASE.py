def swap_case(s):
    s = list(s)
    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122:
            s[i] = chr(ord(s[i])-32)
            #print(s)
            continue
        elif 65 <= ord(s[i]) <= 90:
            s[i] = chr(ord(s[i])+32)
            #continue
        else:
            print()
    #print(rs)
    s = ''.join(s)
    s = s.rstrip()
    #print(s)
    return s

if __name__ == '__main__':
    s = 'Www.HackerRank.com'
    result = swap_case(s)
    print(result)