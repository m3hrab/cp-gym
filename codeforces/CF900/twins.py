import sys

# Constants
INF = float('inf')
MOD = 1000000007

# Faster Input
def read_int():
    return int(sys.stdin.readline())

def read_n_int():
    return map(int, sys.stdin.readline().split())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))


# Faster Output
def print_yes_no(condition):
    print('YES' if condition else 'NO')
    
def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))


# Main Function
def solve():
    n = read_int()
    a = read_ints()
    a.sort()
    count = 0
    temp = 0
    while True:
        temp += a.pop()
        count += 1
        if sum(a) < temp or len(a)==0:
            break 
    
    print(count)

if __name__ == '__main__':
    solve()
