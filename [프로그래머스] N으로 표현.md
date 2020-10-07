# 동적계획법(Dynamic Programming) > N으로 표현
문제 : https://programmers.co.kr/learn/courses/30/lessons/42895

## 문제 설명
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

    12 = 5 + 5 + (5 / 5) + (5 / 5)
    12 = 55 / 5 + 5 / 5
    12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.

이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

## 제한사항
- N은 1 이상 9 이하입니다.
- number는 1 이상 32,000 이하입니다.
- 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
- 최솟값이 8보다 크면 -1을 return 합니다.

## 입출력 예

| N | number | return |
| --- | --- | --- |
| 5 | 12 | 4 |
| 2 | 11 | 3 |

____

> #### < Code : Python >
```python
def solution(N, number):
    answer = -1
    S = [set() for i in range(8)]           # 중복 숫자 포함하지 않기 위해 set사용
    
    for i, value in enumerate(S):
        value.add(int( str(N)*(i+1) ))      # N을 이어붙인 숫자를 추가
        
        for j in range(i):
            for x1 in S[j]:                 # j번째와 i-j번째 집합의 원소 x1과 x2를 꺼내서 연산 
                for x2 in S[i-j-1]:
                    value.add(x1 + x2)
                    value.add(x1 - x2)
                    value.add(x1 * x2)
                    if x2 != 0:
                        value.add(x1 // x2)
        if number in value:                 # number를 찾으면 answer값을 구한 뒤 break
            answer = i + 1
            break
            
    return answer
```

## 문제 리뷰
- N = 5라고 하면, 5를 i번 사용하는 경우는 다음과 같다.
    - i = 1, { 5 }
    - i = 2, { 55, 5+5 (10), 5-5 (0), 5*5 (25), 5/5 (1) }
    - i = 3, { 555, 5+55, 5-55, 5*55, 5/55, 5+10, 5-10, ... }
    - ...
- 이런 식으로, N를 이어붙인 숫자를 제외하고는 x + y = i 가 되는 x번, y번 N을 사용한 집합의 원소끼리의 연산을 이용해 N을 i번 사용하여 구한 원소들을 추가.
- 이때, 중복되는 연산 결과는 포함시키지 않게 하기 위해 S안의 원소를 모두 집합으로 생성.
- N을 이어붙인 숫자를 먼저 추가해준 뒤, 연산을 통한 결과들을 집합 안에 추가.
- bottom-up 방식이기 때문에, 반복 과정 중에 number를 찾는 순간 break.