import sys

"""
1. 구해야 하는 것 : 신입 사원의 최대 인원수
2. 조건 : 서류 심사 성적 or 면접시험 성적이 다른 지원자보다 떨어지지 않는 사람 선발 
ex : 서류 심사 | 면접 심사 
A | 30 | 40 
B | 40 | 50 

=> A는 절대 선발 X 

3. 구해야 하는 값 : [서류 심사 성적, 면접 심사 성적]



""" 
def solve(scores):
    # 1. 우선 서류 심사 성적 순서로 오름차순 정렬
    scores.sort(key = lambda x : x[0])
    count = 0
    # 초기값 setting 
    max_interview_score = 1e9
    for index, score in enumerate(scores):
        if score[1] < max_interview_score:
            count += 1
            max_interview_score = score[1] 
    return count 


if __name__ == "__main__":
    test_cases = int(input())
    answers = []
    for i in range(test_cases):
        appliers = int(input())
        scores = []
        for j in range(appliers): 
            paper, interview = map(int, input().split())
            scores.append((paper, interview)) 
           
        
        answer = solve(scores)
        answers.append(answer)
    
    for answer in answers:
        print(answer)
