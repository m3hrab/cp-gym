"""

/  \     /  |          /  |                         /  |      
$$  \   /$$ |  ______  $$ |____    ______   ______  $$ |____  
$$$  \ /$$$ | /      \ $$      \  /      \ /      \ $$      \ 
$$$$  /$$$$ |/$$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$$  |
$$ $$ $$/$$ |$$    $$ |$$ |  $$ |$$ |  $$/ /    $$ |$$ |  $$ |
$$ |$$$/ $$ |$$$$$$$$/ $$ |  $$ |$$ |     /$$$$$$$ |$$ |__$$ |
$$ | $/  $$ |$$       |$$ |  $$ |$$ |     $$    $$ |$$    $$/ 
$$/      $$/  $$$$$$$/ $$/   $$/ $$/       $$$$$$$/ $$$$$$$/ 
                                    

"""

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
    t = read_ints()

    programmer = []
    mathmaticians = []
    ps = []
    for i in range(n):
        if t[i] == 1:
            programmer.append(i+1)
        elif t[i] == 2:
            mathmaticians.append(i+1)
        else:
            ps.append(i+1)

    m = min(len(programmer), len(mathmaticians), len(ps))
    print(m)
    for i in range(m):
        print("%d %d %d"%(programmer[i],mathmaticians[i],ps[i]))

if __name__ == '__main__':
    solve()
