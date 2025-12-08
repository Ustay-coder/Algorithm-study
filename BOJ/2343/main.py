import sys

def get_prefix_sum(lecture_lengths): 
    prefix_sum = [0] * (len(lecture_lengths) + 1)
    for i in range(len(lecture_lengths)):
        prefix_sum[i + 1] = prefix_sum[i] + lecture_lengths[i]
    return prefix_sum

def solve(lectures, parts, lecture_lengths):
    """
    풀고자 하는 것 : M개의 블루레이 중, 가장 길이가 긴 블루레이 값이 최소가 되는 것. 
    값을 찾아야 하는 범위 : [max(lecture_lengths) ~ sum(lecture_lengths)]

    1. lecture lengths의 누적합 array 생성
    2. 이진 탐색으로 최소 길이 searching 
    """

    left = max(lecture_lengths)
    right = sum(lecture_lengths)
    results = left

    while left <= right:
        mid = (left + right) // 2
        
        bluray_number = 1 
        remain = mid 

        # Remain (블루레이 시간)
        for i in range (lectures):
            if (remain < lecture_lengths[i]):
                remain = mid
                bluray_number += 1
            remain -= lecture_lengths[i]
             
        if (bluray_number <= parts):
            results = mid 
            right = mid - 1
        else :
            left = mid + 1

    print(results)

if __name__ == "__main__":
    lectures, parts = map(int, sys.stdin.readline().split())
    lecture_lengths = list(map(int, sys.stdin.readline().split()))

    solve(lectures, parts, lecture_lengths)