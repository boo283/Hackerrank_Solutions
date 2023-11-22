def average(array):
    # your code goes here
    array = set(array)
    avg = sum(array)/len(array)
    avg = "%.3f" % avg
    return avg
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)