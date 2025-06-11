from tools import timer
from collections import defaultdict
TEST_CASES = [
    "aaaaabbc",
    "abcabcab"
]



# TIME: O(n)
# MEM: O(n)
@timer()
def A(s: str) -> int:
    frq = defaultdict(int)

    for char in s: frq[char] += 1

    frq = list(frq.values())
    e, o = [], []

    for i, even in enumerate(map(lambda x: x % 2 == 0, frq)):
        if even: e.append(frq[i])
        else: o.append(frq[i])

    return max(o) - min(e)

# TIME: O(n)
# MEM: O(n)
@timer()
def B(s: str) -> int:
    frq = defaultdict(int)
    for char in s: frq[char] += 1
    frq = list(frq.values())
    
    return max(frq, key=lambda x: x if x % 2 == 1 else 0) - min(frq, key=lambda x: x if x % 2 == 0 else float('inf'))

# TIME: O(n)
# MEM: O(n)
@timer() # Fastest as only 1 pass of s and frq is made
def C(s: str) -> int:
    frq = defaultdict(int)
    for char in s: frq[char] += 1
    frq = list(frq.values())
    
    maxOdd, minEven = 0, float('inf')
    for i in range(len(frq)):
        val = frq[i]
        if val < minEven and val % 2 == 0: minEven = val
        elif val > maxOdd and val % 2 == 1: maxOdd = val
    return maxOdd - minEven



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        B(test)
        C(test)
        print()