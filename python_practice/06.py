"""
[문제 3]
0부터 26까지의 숫자들로 된 리스트 numbers를 문자로 해독한 뒤 문자들을 더해서 문자열로 반환하는 함수 decode(numbers)를 작성하세요.
숫자 0은 a, 1은 b, ..., 26은 z에 해당됩니다.
"""
number_to_alphabet = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
    6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
    16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
    21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
}

def decode(numbers: list[int]) -> str:
    result = ''
    for i in numbers :
        result += number_to_alphabet[i]
    return result
