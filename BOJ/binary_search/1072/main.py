import sys


def solve(X, Y):
    """
    파라미터 : X(게임 횟수), Y(이긴 게임 횟수)
    구해야 하는 값 : 승률 Z가 변하는 최소 추가 게임 횟수
    구해야 하는 값의 범위 : [1 ~ X]
    """
    z = (Y * 100) // X
    
    if z >= 99:
        print(-1)
        return

    left = 1
    right = X
    result = -1

    while left <= right:
        mid = (left + right) // 2
        # (Y+mid)/(X+mid) * 100
        new_z = ((Y + mid) * 100) // (X + mid)
        
        if new_z > z:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    print(result)


if __name__ == "__main__":
    X, Y = map(int, input().split())
    solve(X, Y)
