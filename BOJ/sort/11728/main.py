import sys


"""
구해야 하는 것 : A, B 합친 후 정렬된 결과

"""
def solve(N, M, A, B):
    
    A.sort()
    B.sort()

    results = []
    pos1 = 0
    pos2 = 0
    while pos1 < N and pos2 < M: 
        if A[pos1] < B[pos2]:
            results.append(A[pos1])
            pos1 += 1
        else:
            results.append(B[pos2])
            pos2 += 1
    
    if pos1 != N: 
        results.extend(A[pos1:])
    if pos2 != M: 
        results.extend(B[pos2:])
    
    for result in results:
        print(result, end=' ')
    


if __name__ == "__main__":

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    solve(N, M,A, B)
