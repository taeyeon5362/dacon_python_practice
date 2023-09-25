"""
[문제 1]
리스트 l1과 l2가 주어졌을 때 l1과 l2의 합집합을 구한 후 리스트로 반환하는 함수 union_of_lists(l1, l2)를 작성하세요.
"""
def union_of_lists(l1: list, l2: list) -> list:
    return list(set(l1)| set(l2))
