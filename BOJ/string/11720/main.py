import sys


def solve(N, numbers):

    sum = 0
    for number in numbers:
        sum += int(number)
    print(sum)


if __name__ == "__main__":
    N = int(input())
    numbers = input()
    solve(N, numbers)
