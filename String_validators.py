if __name__ == '__main__':
    txt = input()
    rs = ['False']*5
    for s in txt:
        if (s.isalnum()):
            rs[0] = 'True'
        if (s.isalpha()):
            rs[1] = 'True'
        if (s.isdigit()):
            rs[2] = 'True'
        if (s.islower()):
            rs[3] = 'True'
        if (s.isupper()):
            rs[4] = 'True'
    print(*rs, sep = '\n')