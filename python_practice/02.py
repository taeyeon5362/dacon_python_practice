"""
[문제 2]
리스트 l이 주어졌을때, 리스트의 처음과 끝을 서로 바꾸어서 반환하는 함수 swap_ends(l)을 작성하세요.
예를 들면 swap_ends([1, 2, 3])의 반환값은 [3, 2, 1]이어야 합니다.
"""
def swap_ends(l: list) -> list:
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp
    
    return l

swap_ends([1, 2, 3])
