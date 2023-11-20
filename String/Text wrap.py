import textwrap

def wrap(string, max_width):
    idx = max_width
    for i in range(len(string)):
        string = string[:idx] + '\n' + string[idx:]
        idx += max_width+1
        if idx >= len(string):
            break
    return string

if __name__ == '__main__':
    string, max_width = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ',4
    result = wrap(string, max_width)
    print(result)