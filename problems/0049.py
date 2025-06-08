from tools import timer
from collections import defaultdict
TEST_CASES = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"]
]



# TIME: O(n*mlogm) | n = len(strs) and m = len(longest string)
# MEM: O(n*m)
@timer(100)
def A(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    for string in strs:
        sort = str(sorted(string))
        res[sort].append(string)
    return list(res.values())

# TIME: O(n*m)
# MEM: O(n*m)
@timer(100)
def B(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    for string in strs:
        key = [0] * 26
        for ch in string: key[ord(ch) - 97] += 1
        res[tuple(key)].append(string)
    return list(res.values())

# TIME: O(n*m)
# MEM: O(n*m)
# Nice solution I saw on Leetcode by Yik Jane and Wenhao | https://leetcode.com/problems/group-anagrams/solutions/6817081/creative-the-mathematical-mindset-that-beats-98-in-both-time-and-space/
@timer(100) # Ignoring prime definitions, better in terms of memory AND faster on larger len(strs)
def C(strs: list[str]) -> list[list[str]]:
    primes = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
    res = defaultdict(list)
    for string in strs:
        key = 1
        for ch in string: key *= primes[ch]
        res[key].append(string)
    return list(res.values())
    # This can quickly run into large keys due to the product nature of key creation



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        B(test)
        C(test)
        print()