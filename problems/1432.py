from tools import timer
TEST_CASES = [
    555,
    9,
    851,
    923,
    1919
]



# TIME: 
# MEM: 
@timer()
def A(num: int) -> int:
    def getMinNum(num: str) -> int:
        minNum = float('inf')
        if int(num[0]) > 1: return int(num.replace(num[0], '1'))
        for char in num[1:]:
            toReplace = num.replace(char, '0')
            if int(toReplace) < minNum and toReplace[0] != '0': minNum = int(toReplace)
        return minNum

    def getMaxNum(num: str) -> int:
        if num[0] != '9': return int(num.replace(num[0], '9'))
        for char in num:
            if char != '9': return int(num.replace(char, '9'))
        return int(num)
    
    num = str(num)
    if len(set(num)) == 1: return int('9' * len(num)) - int('1' * len(num))
    return getMaxNum(num) - getMinNum(num)


if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()