from tools import timer
from collections import defaultdict
TEST_CASES = [
    ("anagram", "nagaram"),
    ("rat", "car")
]



# TIME: O(n*log n)
# MEM: O(1)
@timer()
def A(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    return sorted(s) == sorted(t)

# TIME: O(n)
# MEM: O(n)
@timer()
def B(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    sMap, tMap = defaultdict(int), defaultdict(int)
    for se, te in zip(s,t):
        sMap[se] += 1
        tMap[te] += 1
    return sMap == tMap

# TIME: O(n)
# MEM: O(1)
@timer() # Theoretically best by avoiding sort and inconstant extra space, but slowest for long due to implementations of lists
def C(s: str, t: str) -> bool:
    count = [0] * 26
    for se, te in zip(s, t):
        count[ord(se) - 97] += 1
        count[ord(te) - 97] -= 1
    return all(c == 0 for c in count)



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(*test)
        B(*test)
        C(*test)
        print()