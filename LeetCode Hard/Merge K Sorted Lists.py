# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    adds the first element of each list to the minheap.
    then extracts a elements from the min heap (this elemenet is min of the first elements of all the lists)
    adds that element to a list (which will be the combined new list)
    if the link list (from which we got the value) is not empty it progresses the link list
    and adds the next element of that list to the minheap
    '''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i, linked_list in enumerate(lists):
            if linked_list:
                heapq.heappush(heap, (linked_list.val, i))
        prehead = prev = ListNode(None)
        while len(heap)>0:
            val,i = heapq.heappop(heap)
            prev.next = ListNode(val)
            prev = prev.next
			lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        return prehead.next