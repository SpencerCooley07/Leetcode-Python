from tools import timer
TEST_CASES = [
    "110",
    "001011",
    "101"
    # "00101100101011001011"
]



# TIME: O(n^2)
# MEM: O(n)
@timer() # EXTREMELY SLOW | Very overcomplicated but right idea with L and R sums
def A(boxes: str) -> list[int]:
    res, boxes = [], list(map(int, boxes))
    for x in range(len(boxes)):
        suml = sum([num*(x-i) for i, num in enumerate(boxes[:x])])
        sumr = sum([num*(j+1) for j, num in enumerate(boxes[(x+1):])])
        res.append(suml + sumr)
    return res

# TIME: O(n^2)
# MEM: O(n)
@timer()
def B(boxes: str) -> list[int]:
    n, boxes = len(boxes), list(map(int, boxes))
    res = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n): res[i] += abs(i-j)*boxes[j]
    return res

# TIME: O(n^2)
# MEM: O(n)
@timer() # List comp version of B | Faster on longer strings but slower on shorter ones
def C(boxes: str) -> list[int]:
    n, boxes = len(boxes), list(map(int, boxes))
    return [sum([abs(i-j)*boxes[j] for j in range(n)]) for i in range(n)]

# TIME: O(n)
# MEM: O(n)
@timer() # See explanation below
def D(boxes: str) -> list[int]:
    boxes = list(map(int, boxes))
    l, r = 0, sum(boxes)
    res, operations = [0] * len(boxes), sum(i*box for i, box in enumerate(boxes))
    for i, box in enumerate(boxes):
        res[i] = operations
        if box == 1:
            l, r = l+1, r-1
        operations += l - r
    return res



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        B(test)
        C(test)
        D(test)
        print()



"""
EXPLANATION FOR D
---
- If the pointer shifts to an empty box, the current num of operations should not change
[1,0,0,1,0,0]
 ^              Operations = 3
                Next iteration there will be 1 left and 1 right
[1,0,0,1,0,0]
   ^            Operations = 3 still as left ops += 1 and right ops -= 1

[1,0,0,1,0,0]
     ^          Operations = 3 still

[1,0,0,1,0,0]
       ^        Operations = 3 still BUT next iteration will change |ops|
                Next iteration there will be 2 left and 0 right
[1,0,0,1,0,0]
         ^      Operations = 5

So...
Number of operations doesn't change if number on left == number on right
Operations += (number on left - number on right)
This is because if num on right > num on left, ops decrease by amount extra on right
If num on left > num on right, ops increase by amount extra on left
"""