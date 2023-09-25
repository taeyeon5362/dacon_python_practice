"""
[문제 4]
정수의 리스트 numbers가 주어졌을때, numbers에서 가장 긴 감소하는 시퀀스의 길이를 구하는 함수 lds(numbers)를 작성하세요.
예를 들어, lds([3, 2, 1, 1])에서 가장 긴 감소하는 시퀀스가 3, 2, 1이기 때문에 3이 반환되고,
lds[2, 2, 2, 2]에서 가장 긴 감소하는 시퀀스가 2이기 때문에 1이 반환됩니다.
"""
def lds(numbers: list[int]) -> int:
    ans = 1
    anchor = 0
    for i in range(1, len(numbers)):
        if numbers[i-1] <= numbers[i]: 
            anchor = i
        ans = max(ans, i - anchor + 1)
    return ans
