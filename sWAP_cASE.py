def swap_case(s):
    s = list(s)
    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122:
            s[i] = chr(ord(s[i])-32)
            continue
        elif 65 <= ord(s[i]) <= 90:
            s[i] = chr(ord(s[i])+32)
            continue
        else:
            continue
    s = ''.join(s)
    s = s.rstrip()
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)