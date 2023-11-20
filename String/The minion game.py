def minion_game(string):
    #string = string.replace(' ','')
    vowel =  ['A','E','I','O','U']
    score = [0,0]
    for i in range(len(string)):
        c = string[i]
        if c in vowel:
            score[0]+=len(string[i:])
        else:
            score[1]+=len(string[i:])
    if score[0] > score[1]:
        print("Kevin", score[0])
    elif score[0] < score[1]:
        print("Stuart", score[1])
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)