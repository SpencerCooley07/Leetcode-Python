from tools import timer
from collections import defaultdict
TEST_CASES = [
    (1,10),
    (5,15),
    (19,28),
    (1,100000)
]



# TIME: O(n + log H) | H = highLimit
# MEM: O(n)
@timer
def A(lowLimit: int, highLimit: int) -> int:
    res = defaultdict(lambda: 0)
    for num in [sum(map(int, str(num))) for num in range(lowLimit, highLimit + 1)]: res[num] += 1
    return max(res.values())

# TIME: O(n + log H) | More performant by avoiding str conversions
# MEM: O(n)
@timer
def B(lowLimit: int, highLimit: int) -> int:
    def digitSum(n):
        s = 0
        while n: s, n = s + n % 10, n // 10
        return s
    
    res = defaultdict(lambda: 0)
    for num in [digitSum(num) for num in range(lowLimit, highLimit + 1)]: res[num] += 1
    return max(res.values())

# TIME: O(n + log H) | Same as B
# MEM: O(log H)
@timer
def C(lowLimit: int, highLimit: int) -> int:
    def digitSum(n):
        s = 0
        while n: s, n = s + n % 10, n // 10
        return s
    
    res = defaultdict(lambda: 0)
    for num in range(lowLimit, highLimit + 1): res[digitSum(num)] += 1
    return max(res.values())



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(*test)
        B(*test)
        C(*test)
        print()