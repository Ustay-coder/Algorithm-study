



def binary_search(requests, total):
    """
    찾고자 하는 값 : 최적의 상한액
    탐색 범위 : [0, max(requests)]
    """
    # 초기 값은 requests의 최대값을 선택

    start, end = 0, max(requests)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        
        total_allocated = 0
        for request in requests:
            if request > mid:
                total_allocated += mid
            else:
                total_allocated += request
        
        if total_allocated <= total:
            # result를 저장. start를 증가시켜서 다음 탐색 범위를 좁힌다.
            result = mid
            start = mid + 1
        else:
            # end를 감소시켜서 다음 탐색 범위를 좁힌다.
            end = mid - 1

    return result     

if __name__ == "__main__":

    length = int(input())
    requests = list(map(int ,input().split()))
    total = int(input())

    print(binary_search(requests, total))