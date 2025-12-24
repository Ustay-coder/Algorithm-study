import sys


def solve(N, numbers, v):
    
    count = 0 

    for number in numbers:
        if number == v: 
            count+= 1

  
    print(count)

if __name__ == "__main__":
      # 1. 정수의 개수 입력 
    N = int(input())

    # 2. 정수 입력 
    numbers = list(map(int, input().split()))

    # 3. 찾으려고 하는 정수 v 입력 
    v = int(input())
    solve(N, numbers, v)
