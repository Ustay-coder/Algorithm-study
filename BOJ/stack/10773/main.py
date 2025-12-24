import sys


def solve(N):

    stack = []
    for i in range(N): 
        num = int(input())
        if num == 0: 
            stack.pop()
        else: 
            stack.append(num)

    print(sum(stack))


if __name__ == "__main__":

    N = int(input())
    
    solve(N)
