from tools import timer
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        vals, cur = [], self
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return str(vals)

def linkedList(arr: list) -> list:
    if not arr: return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

TEST_CASES = [
    [1,2,3,4,5],
    [1,2,3,4,5,6]
]



# TIME: O(n)
# MEM: O(n*log n)
@timer()
def A(head: ListNode) -> ListNode:
    res = []
    cur = head
    while cur:
        res.append(cur)
        cur = cur.next
    return res[len(res)//2]

# TIME: O(n)
# MEM: O(1)
@timer() # Two pointer faster one pass approach
def B(head: ListNode):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(linkedList(test))
        B(linkedList(test))
        print()

"""
EXPLANATION FOR B
---
By moving a fast pointer twice as fast as a slow pointer, the slow pointer ends in the middle
[1,2,3,4,5]
 s
 f

[1,2,3,4,5]
   s
     f

[1,2,3,4,5]
     s
         f
Therefore we return the slow pointer

How about for an odd list length?
[1,2,3,4,5,6]
 s
 f

[1,2,3,4,5,6]
   s
     f

[1,2,3,4,5,6]
     s
         f      We still need s to move forward once more, even though f.next.next is None

[1,2,3,4,5,6]
       s
             f
This is our desired slow pointer position

Hence we have found that to move the fast pointer, f.next.next can be None BUT
- f must not be None
- f.next must not be None
"""