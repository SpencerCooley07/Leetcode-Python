from tools import timer
TEST_CASES = [
    ([9,12,5,10,14,3,10], 10),
    ([-3,4,3,2], 2)
]



# TIME: O(n)
# MEM: O(n)
@timer()
def A(nums: list[int], pivot: int) -> list[int]:
    less = [l for l in nums if l < pivot]
    greater = [g for g in nums if g > pivot]
    return less + [pivot]*(len(nums)-(len(less)+len(greater))) + greater

# TIME: O(n) | Less full passes over n hence lower constant k in O(k*n)
# MEM: O(n)
@timer()
def B(nums: list[int], pivot: int) -> list[int]:
    less, equal, greater = [], [], []
    for num in nums:
        if num < pivot: less.append(num)
        elif num > pivot: greater.append(num)
        else: equal.append(num)
    return less + equal + greater



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(*test)
        B(*test)
        print()